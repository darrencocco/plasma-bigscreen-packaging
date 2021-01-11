Summary: Settings module for Plasma Mobile.
Name: plasma-settings
Version: 0.1.0
Release: 1
License: GPLv2
Source: https://invent.kde.org/plasma-mobile/plasma-settings/-/archive/master/plasma-settings-master.tar.gz
URL: https://invent.kde.org/plasma-mobile/plasma-settings
Distribution: Fedora
Packager: Darren Cocco <linux.fedora.packages@darren.cocco.id.au>

Requires: kf5-kconfig
Requires: kf5-solid
Requires: kf5-kauth
Requires: kf5-kdbusaddons
Requires: kf5-ki18n
Requires: kf5-plasma
Requires: kf5-kdeclarative
Requires: kf5-kio
Requires: gettext
Requires: gobject-introspection

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kio-devel
BuildRequires: gettext
BuildRequires: gobject-introspection

%description
Settings module for Plasma Mobile.

%prep
%setup -n %{name}-master

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%dir /usr/share/kpackage/genericqml/org.kde.plasma.settings
%dir /usr/share/kpackage/genericqml/org.kde.plasma.settings/contents
%dir /usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/KCMContainer.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/ModulesList.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/main.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/metadata.desktop
/usr/share/applications/org.kde.mobile.plasmasettings.desktop
/usr/bin/plasma-settings
/usr/share/kservices5/themesettings.desktop
/usr/lib64/qt5/plugins/kcms/kcm_mobile_theme.so
%dir /usr/share/kpackage/kcms/kcm_mobile_theme
%dir /usr/share/kpackage/kcms/kcm_mobile_theme/contents
%dir /usr/share/kpackage/kcms/kcm_mobile_theme/contents/ui
/usr/share/kpackage/kcms/kcm_mobile_theme/contents/ui/Theme.qml
/usr/share/kpackage/kcms/kcm_mobile_theme/metadata.desktop
/usr/share/kpackage/kcms/kcm_mobile_theme/metadata.json
/usr/share/kservices5/timesettings.desktop
/usr/lib64/qt5/plugins/kcms/kcm_mobile_time.so
%dir /usr/share/kpackage/kcms/kcm_mobile_time
%dir /usr/share/kpackage/kcms/kcm_mobile_time/contents
%dir /usr/share/kpackage/kcms/kcm_mobile_time/contents/ui
/usr/share/kpackage/kcms/kcm_mobile_time/contents/ui/DatePicker.qml
/usr/share/kpackage/kcms/kcm_mobile_time/contents/ui/Digit.qml
/usr/share/kpackage/kcms/kcm_mobile_time/contents/ui/Time.qml
/usr/share/kpackage/kcms/kcm_mobile_time/contents/ui/TimePicker.qml
/usr/share/kpackage/kcms/kcm_mobile_time/metadata.desktop
/usr/share/kpackage/kcms/kcm_mobile_time/metadata.json
/usr/lib64/qt5/plugins/kcms/kcm_mobile_info.so
/usr/share/kservices5/info.desktop
%dir /usr/share/kpackage/kcms/kcm_mobile_info
%dir /usr/share/kpackage/kcms/kcm_mobile_info/contents
%dir /usr/share/kpackage/kcms/kcm_mobile_info/contents/ui
/usr/share/kpackage/kcms/kcm_mobile_info/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_mobile_info/metadata.desktop
/usr/share/kpackage/kcms/kcm_mobile_info/metadata.json
/usr/lib64/qt5/plugins/kcms/kcm_mobile_cellularnetwork.so
/usr/share/kservices5/cellularnetwork.desktop
%dir /usr/share/kpackage/kcms/kcm_mobile_cellularnetwork
%dir /usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents
%dir /usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui/Contexts.qml
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui/Modems.qml
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui/Registrations.qml
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui/SimCards.qml
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/metadata.desktop
/usr/share/kpackage/kcms/kcm_mobile_cellularnetwork/metadata.json
/usr/lib64/qt5/plugins/kcms/kcm_mobile_virtualkeyboard.so
/usr/share/kservices5/kcm_mobile_virtualkeyboard.desktop
%dir /usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard
%dir /usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/contents
%dir /usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/contents/ui
/usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/contents/ui/languages.qml
/usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/metadata.desktop
/usr/share/kpackage/kcms/kcm_mobile_virtualkeyboard/metadata.json
/usr/share/kservices5/kcm_password.desktop
/usr/lib64/qt5/plugins/kcms/kcm_password.so
/usr/share/kpackage/kcms/kcm_password
%dir /usr/share/kpackage/kcms/kcm_password/contents
%dir /usr/share/kpackage/kcms/kcm_password/contents/ui
/usr/share/kpackage/kcms/kcm_password/contents/ui/Password.qml
/usr/share/kpackage/kcms/kcm_password/metadata.desktop
/usr/share/kpackage/kcms/kcm_password/metadata.json

