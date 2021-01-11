Summary: User interface for Mycroft assistant.
Name: mycroft-gui
Version: 1.0.1
Release: 1
License: APLv2
Source: https://github.com/MycroftAI/mycroft-gui/archive/v1.0.1.tar.gz
URL: https://mycroft.ai/
Distribution: Fedora
Packager: Darren Cocco <linux.fedora.packages@darren.cocco.id.au>

Suggests: mycroft-core

Requires: kf5-kio-core
Requires: kio-extras
Requires: kf5-plasma
Requires: kf5-kdbusaddons
Requires: kf5-ki18n
Requires: qt5-qtwebsockets
Requires: qt5-qtwebview
Requires: qt5-qtdeclarative
Requires: qt5-qtmultimedia
Requires: qt5-qtquickcontrols2
Requires: qt5-qtwebengine
Requires: qt5-qtbase

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: kf5-kio-devel
BuildRequires: kio-extras-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtwebview-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: gettext


%description
Graphical user interface for Mycroft.

%prep
%setup

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
/usr/bin/mycroft-gui-core-loader
/usr/bin/mycroft-gui-core-stop
/usr/bin/mycroft-gui-app
/usr/share/applications/ai.mycroft.gui-app.desktop
/usr/share/icons/hicolor/16x16/apps/mycroft.svg
/usr/share/icons/hicolor/32x32/apps/mycroft.svg
/usr/lib64/qt5/qml/Mycroft/libmycroftplugin.so
/usr/lib64/qt5/qml/Mycroft/qmldir
%dir /usr/lib64/qt5/qml/Mycroft
/usr/lib64/qt5/qml/Mycroft/AudioPlayer.qml
/usr/lib64/qt5/qml/Mycroft/Delegate.qml
/usr/lib64/qt5/qml/Mycroft/PaginatedText.qml
/usr/lib64/qt5/qml/Mycroft/ScrollableDelegate.qml
/usr/lib64/qt5/qml/Mycroft/SkillView.qml
/usr/lib64/qt5/qml/Mycroft/SlideShow.qml
/usr/lib64/qt5/qml/Mycroft/SlidingImage.qml
/usr/lib64/qt5/qml/Mycroft/VideoPlayer.qml
%dir /usr/lib64/qt5/qml/Mycroft/private
/usr/lib64/qt5/qml/Mycroft/private/ImageBackground.qml
/usr/lib64/qt5/qml/Mycroft/AutoFitLabel.qml
/usr/lib64/qt5/qml/Mycroft/ProportionalDelegate.qml
/usr/lib64/qt5/qml/Mycroft/StatusIndicator.qml
