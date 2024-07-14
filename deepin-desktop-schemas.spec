Name:           deepin-desktop-schemas
Version:        6.0.6
Release:        1
Summary:        GSettings deepin desktop-wide schemas
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# export GOPATH=`pwd`/.godeps
# go mod download
Source1:	deepin-desktop-schemas-6.0.6-godeps.tar.xz

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  pkgconfig(glib-2.0)
#add jzy
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang-deepin-go-lib
#BuildRequires:  golang(github.com/linuxdeepin/go-lib/keyfile)
BuildRequires:  make

Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-icon-theme
Requires:       deepin-sound-theme
Obsoletes:      deepin-artwork-themes

%description
%{summary}.

%prep
%autosetup -p1
tar xf %{S:1}

# fix default background url
#sed -i '/picture-uri/s|default_background.jpg|default.png|' \
#    overrides/common/com.deepin.wrap.gnome.desktop.override
#sed -i 's|python|python3|' Makefile tools/overrides.py
# connectivity check uri copy from /usr/lib/NetworkManager/conf.d/20-connectivity-fedora.conf
#sed -i "s#'http://detect.uniontech.com', 'http://detectportal.deepin.com'#'http://fedoraproject.org/static/hotspot.txt'#" \
#    schemas/com.deepin.dde.network-utils.gschema.xml
#grep uniontech schemas/com.deepin.dde.network-utils.gschema.xml && exit 1 || :

%build
GOPATH=`pwd`/.godeps:%{gopath} %make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/deepin-appstore/
%{_datadir}/deepin-app-store/
%{_datadir}/%{name}/
