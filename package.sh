#!/bin/bash
#
# This script generates RPM and debian packages.
#
# Usage: ./package.sh [VERSION_TAG]
# Usage: ./package.sh [-t] [VERSION_TAG]
#
#
#   -t: use timestamp based package name for unstable packges.
#
#   VERSION_TAG: Tag to determine version and revision string for
#                deb and RPM packages
#                If ommited (recommended), it defaults to
#                `git describe --tags`
#
# Build ependencies:
#   In short, do the following on Ubuntu based distribution to install
#   build dependencies.
#
#   $ sudo apt-get install -y rubygems rpm ruby-ronn && sudo gem install fpm
#
#   Here's list of dependencies:
#
#   * fpm (https://github.com/jordansissel/fpm):
#       This enables us to produce both RPM and debian packages easily
#       withough requiring details about their packaging systems
#
#   * rpm: of course rpmbuild is needed to produce RPM packages
#
#   * ronn: a tool to produce man pages from markdown

set -e

while getopts t OPT; do
    case "$OPT" in
      t)
          USE_TIMESTAMP=yes
          shift
          ;;
    esac
done

# Get version tag from command line or defaults to use git describe
version_tag=$1
if [ "$version_tag" == "" ]; then
    version_tag=$(git describe --tags)
fi

if [[ "$version_tag" =~ v([0-9.]*)$ ]]; then
    # For official release, e.g. v1.8.0
    echo "Packaging official release: $version_tag"
    version=${BASH_REMATCH[1]}

    rpm_version=$version
    rpm_revision=1

    deb_version=$version
    deb_revision=1

elif [[ "$version_tag" =~ v([0-9.]*)-(rc[0-9]+)$ ]]; then
    # For RC packages, e.g. v1.8.0-rc1
    echo "Producing RC packages for " $version_tag
    version=${BASH_REMATCH[1]}
    rc_tag=${BASH_REMATCH[2]}

    rpm_version=$version
    rpm_revision="0."$rc_tag

    deb_version=$version~$rc_tag
    deb_revision=1

elif [[ "$version_tag" =~ v([0-9.]*)-(rc[0-9]+.*)$ ]]; then
    # For unstable packages, e.g.v1.8.0-rc0-4-g994371d with git describe --tags
    echo Producing unstable packages for tag: $version_tag
    version=${BASH_REMATCH[1]}

    if [ "$USE_TIMESTAMP" == "yes" ]; then
        pre_release_tag=$(date '+%Y%m%d%H%M')
    else
        pre_release_tag=$(echo ${BASH_REMATCH[2]} | sed -e 's/-/./g')
    fi

    rpm_version=$version
    rpm_revision="0".$pre_release_tag

    deb_version=$version~$pre_release_tag
    deb_revision=1

else
    echo "Aborted. invalid version tag. $version_tag"
    exit 1
fi


echo "Packaging with the following info"
echo "RPM: version=$rpm_version, revision=$rpm_revision"
echo "DEB: version=$deb_version, revision=$deb_revision"

## Common args for rpm and deb
FPM_BASE_ARGS=$(cat <<EOF
--name 'python-midonetclient' \
--architecture 'noarch' \
--license 'Apache License, Version 2.0' \
--vendor 'MidoNet' \
--maintainer "Midokura" \
--url 'http://midonet.org' \
--description 'Python client library for MidoNet API' \
-d 'python-webob' -d 'python-eventlet' -d 'python-httplib2' \
-s dir
EOF
)

function clean() {
    find . -name "*.pyc" -exec rm {} \;
    rm -f doc/*.{gz,.1}
    rm -rf build
}

function build_man_pages() {
    ronn --roff doc/*.ronn 2> /dev/null
    gzip -f doc/*.1
}

function package_rpm() {
    RPM_BUILD_DIR=build/rpm/
    mkdir -p  $RPM_BUILD_DIR/usr/lib/python2.6/site-packages/
    mkdir -p  $RPM_BUILD_DIR/usr/lib/python2.7/site-packages/
    mkdir -p  $RPM_BUILD_DIR/usr/bin/
    mkdir -p  $RPM_BUILD_DIR/usr/share/man/man1

    cp -r  src/midonetclient $RPM_BUILD_DIR/usr/lib/python2.6/site-packages/
    cp -r  src/midonetclient $RPM_BUILD_DIR/usr/lib/python2.7/site-packages/
    cp src/bin/midonet-cli $RPM_BUILD_DIR/usr/bin/
    cp doc/*.gz $RPM_BUILD_DIR/usr/share/man/man1/
    RPM_ARGS="$RPM_ARGS -v $rpm_version"
    RPM_ARGS="$RPM_ARGS -C build/rpm"
    RPM_ARGS="$RPM_ARGS -d 'python >= 2.6' -d 'python < 2.8'"
    RPM_ARGS="$RPM_ARGS --epoch 1"
    RPM_ARGS="$RPM_ARGS --iteration $rpm_revision"
    eval fpm $FPM_BASE_ARGS $RPM_ARGS -t rpm .
}

function package_deb() {
    DEB_BUILD_DIR=build/deb
    mkdir -p  $DEB_BUILD_DIR/usr/lib/python2.7/dist-packages
    mkdir -p  $DEB_BUILD_DIR/usr/bin/
    mkdir -p  $DEB_BUILD_DIR/usr/share/man/man1/

    cp -r  src/midonetclient $DEB_BUILD_DIR/usr/lib/python2.7/dist-packages
    cp src/bin/midonet-cli $DEB_BUILD_DIR/usr/bin/
    cp doc/*.gz $DEB_BUILD_DIR/usr/share/man/man1/

    DEB_ARGS="$DEB_ARGS -v $deb_version"
    DEB_ARGS="$DEB_ARGS -C build/deb"
    DEB_ARGS="$DEB_ARGS --deb-priority optional"
    DEB_ARGS="$DEB_ARGS --iteration $deb_revision"

    eval fpm $FPM_BASE_ARGS $DEB_ARGS -t deb .
}

# Main
clean
build_man_pages
package_rpm
package_deb
