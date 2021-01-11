Summary: Plasma Nano shell for embedded devices.
Name: plasma-nano
Version: 5.20.4
Release: 1
License: GPLv2
Source: https://invent.kde.org/plasma/plasma-nano/-/archive/v5.20.4/plasma-nano-v5.20.4.tar.gz
URL:  https://invent.kde.org/plasma/plasma-nano
Distribution: Fedora
Packager: Darren Cocco <linux.fedora.packages@darren.cocco.id.au>

Requires: kf5-plasma >= 5.74
Requires: kf5-kwayland >= 5.74
Requires: kf5-kwindowsystem >= 5.74
Requires: kf5-kservice >= 5.75.0
Requires: kf5-kcoreaddons >= 5.75.0
Requires: kf5-kpackage >= 5.75.0
Requires: qt5-qtdeclarative

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: kf5-plasma-devel >= 5.74
BuildRequires: kf5-kwayland-devel >= 5.74
BuildRequires: kf5-kwindowsystem-devel >= 5.74
BuildRequires: kf5-kservice-devel >= 5.75.0
BuildRequires: kf5-kcoreaddons-devel >= 5.75.0
BuildRequires: kf5-kpackage-devel >= 5.75.0
BuildRequires: qt5-qtdeclarative-devel

%description
A minimalist Plasma shell for developing custom
experiences on embedded devices.

%prep
%setup -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%dir /usr/share/plasma/shells/org.kde.plasma.nano
%dir /usr/share/plasma/shells/org.kde.plasma.nano/contents
%dir /usr/share/plasma/shells/org.kde.plasma.nano/contents/applet
/usr/share/plasma/shells/org.kde.plasma.nano/contents/applet/AppletError.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/applet/CompactApplet.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/applet/DefaultCompactRepresentation.qml
%dir /usr/share/plasma/shells/org.kde.plasma.nano/contents/configuration
/usr/share/plasma/shells/org.kde.plasma.nano/contents/configuration/AppletConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/configuration/ConfigCategoryDelegate.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/configuration/ConfigurationContainmentAppearance.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/configuration/ContainmentConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/defaults
%dir /usr/share/plasma/shells/org.kde.plasma.nano/contents/explorer
/usr/share/plasma/shells/org.kde.plasma.nano/contents/explorer/AppletDelegate.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/explorer/WidgetExplorer.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/layout.js
/usr/share/plasma/shells/org.kde.plasma.nano/contents/loader.qml
%dir /usr/share/plasma/shells/org.kde.plasma.nano/contents/views
/usr/share/plasma/shells/org.kde.plasma.nano/contents/views/Desktop.qml
/usr/share/plasma/shells/org.kde.plasma.nano/contents/views/Panel.qml
/usr/share/plasma/shells/org.kde.plasma.nano/metadata.desktop
/usr/share/plasma/shells/org.kde.plasma.nano/metadata.json
/usr/share/kservices5/plasma-applet-org.kde.plasma.nano.desktop
%dir /usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox
%dir /usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/contents
%dir /usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/contents/ui
/usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/contents/ui/DesktopConfigButtons.qml
/usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/contents/ui/ToolBoxRoot.qml
/usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/metadata.desktop
/usr/share/plasma/packages/org.kde.plasma.nano.desktoptoolbox/metadata.json
/usr/share/metainfo/org.kde.plasma.nano.desktoptoolbox.appdata.xml
/usr/share/kservices5/plasma-package-org.kde.plasma.nano.desktoptoolbox.desktop
/usr/lib64/qt5/qml/org/kde/plasma/private/nanoshell/libplasmananoshellprivateplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/private/nanoshell/qmldir
%dir /usr/lib64/qt5/qml/org/kde/plasma/private/nanoshell/qml
/usr/lib64/qt5/qml/org/kde/plasma/private/nanoshell/qml/StartupFeedback.qml
