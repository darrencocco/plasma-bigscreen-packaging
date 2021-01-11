Summary: Plasma workspace for TV screens.
Name: plasma-bigscreen
Version: 0.0.2
Release: 1
License: GPLv2
Source: https://invent.kde.org/plasma/plasma-bigscreen/-/archive/master/plasma-bigscreen-master.tar.gz
URL: https://plasma-bigscreen.org/
Distribution: Fedora
Packager: Darren Cocco <linux.fedora.packages@darren.cocco.id.au>

Requires: mycroft-gui
Requires: plasma-nano

Requires: kf5-kactivities
Requires: kf5-kactivities-stats
Requires: kf5-plasma
Requires: kf5-ki18n
Requires: kf5-kirigami2
Requires: kf5-kdeclarative
Requires: kf5-kcmutils
Requires: kf5-knotifications
Requires: kf5-kio
Requires: kf5-kwayland
Requires: kf5-kwindowsystem
Requires: plasma-workspace
Requires: qt5-qtmultimedia
Requires: kdeconnectd
Requires: plasma-nm
Requires: kde-settings-pulseaudio
Requires: plasma-settings

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: mycroft-gui

BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kactivities-stats-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kirigami2-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: plasma-workspace-devel
BuildRequires: qt5-qtmultimedia-devel

%description
A KDE Plasma workspace designed for use on
TV screens. Uses Mycroft to provide voice
based controls.

%prep
%setup -n %{name}-master

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%dir /usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen
%dir /usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents
%dir /usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/AppletConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ConfigCategoryDelegate.qml
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ConfigurationContainmentAppearance.qml
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ContainmentConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/SlideshowThumbnail.png
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/WallpaperDelegate.qml
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/defaults
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/layout.js
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/metadata.desktop
/usr/share/plasma/shells/org.kde.plasma.mycroft.bigscreen/metadata.json
/usr/share/metainfo/org.kde.plasma.mycroft.bigscreen.appdata.xml
/usr/share/kservices5/plasma-applet-org.kde.plasma.mycroft.bigscreen.desktop
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/defaults
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/layouts
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/layouts/org.kde.plasma.mycroft.bigscreen-layout.js
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/lockscreen
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/lockscreen/LockScreen.qml
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/previews
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/previews/splash.png
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/Splash.qml
%dir /usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/busycolored.svg
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/busywidget.svgz
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/kde.svgz
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/logo-big.svg
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/logo.svg
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/plasma.svgz
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/rocket.svg
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/metadata.desktop
/usr/share/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/metadata.json
/usr/share/kservices5/plasma-lookandfeel-org.kde.plasma.mycroft.bigscreen.desktop
/usr/bin/mycroft-skill-launcher.py
/usr/bin/plasma-bigscreen-wayland
/usr/share/wayland-sessions/plasma-bigscreen-wayland.desktop
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/config
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/config/main.xml
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/ConfigWindow.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/MycroftIndicator.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/MycroftWindow.qml
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/AbstractIndicator.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/KdeConnect.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/MycroftConnect.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/PairWindow.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Shutdown.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Volume.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Wifi.qml
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/code
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/code/icon.js
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/FeedbackWindow.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/LauncherHome.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/LauncherMenu.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/PlaceHolderPage.qml
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/config
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/config/configGeneral.qml
%dir /usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/AppDelegate.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/SettingDelegate.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/VoiceAppDelegate.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/metadata.json
/usr/share/metainfo/org.kde.mycroft.bigscreen.homescreen.appdata.xml
/usr/share/kservices5/plasma-applet-org.kde.mycroft.bigscreen.homescreen.desktop
/usr/lib64/qt5/plugins/plasma/applets/plasma_containment_biglauncherhomescreen.so
/usr/lib64/qt5/plugins/kcms/kcm_audiodevice.so
/usr/share/kservices5/kcm_audiodevice.desktop
%dir /usr/share/kpackage/kcms/kcm_audiodevice
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents/ui
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/DeviceChooserPage.qml
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/SettingsItem.qml
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/code
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/code/icon.js
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/delegates
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/delegates/AudioDelegate.qml
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/delegates/CompactAudioDelegate.qml
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/delegates/VolumeObject.qml
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/images
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/images/green-tick-thick.svg
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/images/green-tick.svg
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/main.qml
%dir /usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/views
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/views/RowLabelView.qml
/usr/share/kpackage/kcms/kcm_audiodevice/contents/ui/views/TileView.qml
/usr/share/kpackage/kcms/kcm_audiodevice/metadata.desktop
/usr/share/kpackage/kcms/kcm_audiodevice/metadata.json
%dir /usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/KCMContainer.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/ModulesList.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/VirtualKeyboard.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/VirtualKeyboardLoader.qml
/usr/share/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/main.qml
/usr/lib64/qt5/plugins/kcms/kcm_mediacenter_wifi.so
/usr/share/kservices5/mediacenter_wifi.desktop
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/DetailsText.qml
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/DeviceConnectionItem.qml
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/NetworkItem.qml
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/delegates
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/delegates/CompactNetworkDelegate.qml
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/delegates/NetworkDelegate.qml
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/images
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/images/green-tick-thick.svg
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/images/green-tick.svg
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/main.qml
%dir /usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/views
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/views/RowLabelView.qml
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/metadata.desktop
/usr/share/kpackage/kcms/kcm_mediacenter_wifi/metadata.json
/usr/lib64/qt5/plugins/kcms/kcm_mediacenter_kdeconnect.so
/usr/share/kservices5/mediacenter_kdeconnect.desktop
%dir /usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect
%dir /usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents
%dir /usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/DeviceConnectionView.qml
%dir /usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/DeviceDelegate.qml
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/PairRequest.qml
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/PairedView.qml
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/UnpairedView.qml
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/Unreachable.qml
%dir /usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/images
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/images/green-tick-thick.svg
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/images/green-tick.svg
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/metadata.desktop
/usr/share/kpackage/kcms/kcm_mediacenter_kdeconnect/metadata.json
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/libbigscreenplugin.so
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/qmldir
%dir /usr/lib64/qt5/qml/org/kde/mycroft/bigscreen
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/AbstractDelegate.qml
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/IconDelegate.qml
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/NavigationSoundEffects.qml
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/TileRepeater.qml
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/TileView.qml
/usr/lib64/qt5/qml/org/kde/mycroft/bigscreen/background.svg
%dir /usr/share/sounds/plasma-bigscreen
/usr/share/sounds/plasma-bigscreen/clicked.wav
/usr/share/sounds/plasma-bigscreen/moving.wav
