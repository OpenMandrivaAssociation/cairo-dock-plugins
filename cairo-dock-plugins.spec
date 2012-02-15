%define packagename cairo-dock

Summary:	Plugins for cairo-dock
Name:     	cairo-dock-plugins
Version:	2.4.0
Release:	2
License:	GPLv3+
Group:		Graphical desktop/Other
Source0: 	http://launchpadlibrarian.net/70938279/%{name}-%{version}~2.tar.gz
URL:		https://launchpad.net/cairo-dock-plug-ins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cairo-dock = %{version}
BuildRequires:	cairo-dock-devel = %{version}
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	libdbus-1-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	vte-devel
BuildRequires:	fftw3-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	libalsa-devel
BuildRequires:	cairo-devel
BuildRequires:	thunar-devel
BuildRequires:	intltool
BuildRequires:	gnutls-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	libxklavier-devel
BuildRequires:	libetpan-devel
BuildRequires:	webkitgtk-devel
BuildRequires:	libexif-devel
BuildRequires:	libical-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	libetpan-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	glib-sharp2
BuildRequires:	ruby
BuildRequires:	UPower-devel
BuildRequires:	libdbusmenu-gtk-devel
%if %mdkversion >= 201100
BuildRequires:	ndesk-dbus-glib-devel
BuildRequires:	zeitgeist-devel
BuildRequires:	vala
%endif
Requires:	%{packagename}-clock
Requires:	%{packagename}-dustbin
Requires:	%{packagename}-logout
Requires:	%{packagename}-musicPlayer
Requires:	%{packagename}-rendering
Requires:	%{packagename}-terminal
Requires:	%{packagename}-powermanager
Requires:	%{packagename}-shortcuts
Requires:	%{packagename}-systray
Requires:	%{packagename}-weather
Requires:	%{packagename}-xgamma
Requires:	%{packagename}-alsamixer
Requires:	%{packagename}-cairo-penguin
Requires:	%{packagename}-tomboy
Requires:	%{packagename}-wifi
Requires:	%{packagename}-netspeed
Requires:	%{packagename}-switcher
Requires:	%{packagename}-dbus
Requires:	%{packagename}-showdesktop
Requires:	%{packagename}-slider
Requires:	%{packagename}-stack
Requires:	%{packagename}-System-monitor
Requires:	%{packagename}-clipper
Requires:	%{packagename}-animated-icons
Requires:	%{packagename}-desklet-rendering
Requires:	%{packagename}-dialog-rendering
Requires:	%{packagename}-drop_indicator
Requires:	%{packagename}-icon-effect
Requires:	%{packagename}-illusion
Requires:	%{packagename}-motion_blur
Requires:	%{packagename}-quick-browser
Requires:	%{packagename}-show_mouse
Requires:	%{packagename}-toons
Requires:	%{packagename}-keyboard-indicator
Requires:	%{packagename}-weblets
Requires:	%{packagename}-dnd2share
Requires:	%{packagename}-kde-integration
Requires:	%{packagename}-mail
Requires:	%{packagename}-rssreader
Requires:	%{packagename}-impulse
Requires:	%{packagename}-Folders
Requires:	%{packagename}-remote-control
Requires:	%{packagename}-composite-manager
Obsoletes:	%{packagename}-showdesklets < 2.1.3

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package contains various plugins for cairo-dock.

%files
%defattr(-, root, root)

#---------------------------------------------------------------------
%package i18n
Summary: Translation files for %{name}
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description i18n
This package contains common translations for %{name}.

%files i18n -f %{name}.lang
%defattr(-, root, root)

#---------------------------------------------------------------------
%package -n %{packagename}-animated-icons
Summary: That package provides plugin "Animated icons"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-animated-icons
This plug-in provides many different animations for your icons.

%files -n %{packagename}-animated-icons
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Animated-icons
%{_libdir}/cairo-dock/libcd-Animated-icons.so

#---------------------------------------------------------------------
%package -n %{packagename}-clock
Summary: That package provides plugin "clock"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-clock
Display rime and date in your dock with the clock applet!
2 view are available: numeric and analogic.
It can derach itself to be the perfect clone of CairoClock.
It can warn you with alarms, can display a calendar, and
allow you to setup time and date.

%files -n %{packagename}-clock
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/clock
%{_libdir}/cairo-dock/libcd-clock.so

#---------------------------------------------------------------------
%package -n %{packagename}-desklet-rendering
Summary: That package provides plugin "desklet-rendering"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-desklet-rendering
This module provides different views for your desklets.

%files -n %{packagename}-desklet-rendering
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/desklet-rendering
%{_libdir}/cairo-dock/libcd-desklet-rendering.so

#---------------------------------------------------------------------
%package -n %{packagename}-dialog-rendering
Summary: That package provides plugin "dialog-rendering"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-dialog-rendering
This plug-in provides some dialog decorators for dialog bubbles.

%files -n %{packagename}-dialog-rendering
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/dialog-rendering
%{_libdir}/cairo-dock/libcd-dialog-rendering.so

#---------------------------------------------------------------------
%package -n %{packagename}-dnd2share
Summary: That package provides plugin "dnd2share"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-dnd2share
This applet lets you share files easily :
Drag-and-drop a file on the icon to upload it to one of the available hosting sites.
It supports many sites, like DropBox, Imageshack, pastebin, etc
You can upload text, image, video, and files.
The resulting URL is automatically stored in the clipboard to be directly copied by CTRL+v.
It can keep an history of your last uploads to retrieve them without any account.
You'll need to install 'curl' and 'wget' to upload the data.

%files -n %{packagename}-dnd2share
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/dnd2share
%{_libdir}/cairo-dock/libcd-dnd2share.so

#---------------------------------------------------------------------
%package -n %{packagename}-drop_indicator
Summary: That package provides plugin "drop_indicator"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-drop_indicator
This plug-in displays an animated indicator when you drop something in the dock.

%files -n %{packagename}-drop_indicator
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/drop-indicator
%{_libdir}/cairo-dock/libcd-drop_indicator.so

#---------------------------------------------------------------------
%package -n %{packagename}-dustbin
Summary: That package provides plugin "dustbin"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-dustbin
Manage your disks space with this trash applet!
It can handle several trash directories,
threw files or unmount diisks with drag'n'drop,
warn you if you use too much space,
and display usefull info about your dustbins.

%files -n %{packagename}-dustbin
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/dustbin
%{_libdir}/cairo-dock/libcd-dustbin.so

#---------------------------------------------------------------------
%package -n %{packagename}-icon-effect
Summary: That package provides plugin "icon-effect"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-icon-effect
This plug-in adds many special effects to your icons.

%files -n %{packagename}-icon-effect
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/icon-effect
%{_libdir}/cairo-dock/libcd-icon-effect.so

#---------------------------------------------------------------------
%package -n %{packagename}-illusion
Summary: That package provides plugin "illusion"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-illusion
This plug-in provides animations for appearance & disappearance of icons.

%files -n %{packagename}-illusion
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/illusion
%{_libdir}/cairo-dock/libcd-illusion.so

#---------------------------------------------------------------------
%package -n %{packagename}-kde-integration
Summary: That package provides plugin "kde-integration"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-kde-integration
This applet provides functions for a better integration into a KDE environnement.
It is auto-activated, so you don't need to activate it.
It is designed for KDE4.

%files -n %{packagename}-kde-integration
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/kde-integration
%{_libdir}/cairo-dock/libcd_kde-integration.so

#---------------------------------------------------------------------
%package -n %{packagename}-logout
Summary: That package provides plugin "logout"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-logout
A very simple applet that adds an icon to log out
from your session.

%files -n %{packagename}-logout
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/logout
%{_libdir}/cairo-dock/libcd-logout.so

#---------------------------------------------------------------------
%package -n %{packagename}-mail
Summary: That package provides plugin "mail"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-mail
This applet is very useful to warn you when you get new e-mails
It can check in any kind of mailbox (yahoo, gmail, etc)
Left-click to launch the prefered mail application,
Middle-click to refresh all the mailboxes.

%files -n %{packagename}-mail
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/mail
%{_libdir}/cairo-dock/libcd-mail.so

#---------------------------------------------------------------------
%package -n %{packagename}-motion_blur
Summary: That package provides plugin "motion_blur"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-motion_blur
This plug-in adds a motion blur effect on docks.

%files -n %{packagename}-motion_blur
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/motion-blur
%{_libdir}/cairo-dock/libcd-motion_blur.so

#---------------------------------------------------------------------
%package -n %{packagename}-musicPlayer
Summary: That package provides plugin "musicPlayer"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}
Obsoletes: %{packagename}-rhythmbox < 2.1.2
Obsoletes: %{packagename}-xmms < 2.1.2

%description -n %{packagename}-musicPlayer
This applet lets you control any music player.
Left click to Play/Pause, middle-click to play Next song. Scroll up/down
to play previous/next song. You can drag and drop songs on the icon to
put them in the queue,and jpeg image to use as cover.

%files -n %{packagename}-musicPlayer
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/musicPlayer
%{_libdir}/cairo-dock/libcd-musicPlayer.so

#---------------------------------------------------------------------
%package -n %{packagename}-quick-browser
Summary: That package provides plugin "quick-browser"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-quick-browser
This applet lets you browse a folder and its sub-folders very quickly.
You can set up a shortkey to pop up the menu. Midlle-click will open
the main folder.
This applet can be instanciated several times, if you want to browse
different folders.

%files -n %{packagename}-quick-browser
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/quick_browser
%{_libdir}/cairo-dock/libcd-quick-browser.so

#---------------------------------------------------------------------
%package -n %{packagename}-rendering
Summary: That package provides plugin "rendering"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-rendering
This module adds different views to your dock.
Any dock or sub-dock can be displayed with the
view of your choice. Currently, 3D-plane, Caroussel,
Parabolic and Rainbow views are provided

%files -n %{packagename}-rendering
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/rendering
%{_libdir}/cairo-dock/libcd-rendering.so

#---------------------------------------------------------------------
%package -n %{packagename}-terminal
Summary: That package provides plugin "terminal"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-terminal
Add a terminal to your dock!
You can drag'n'drop files or text into it
and select an action

%files -n %{packagename}-terminal
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/terminal
%{_libdir}/cairo-dock/libcd-terminal.so

#---------------------------------------------------------------------
%package -n %{packagename}-powermanager
Summary: That package provides a powermanager plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-powermanager
A power manager for laptop's battery
It works with ACPI and DBus.

%files -n %{packagename}-powermanager
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/powermanager
%{_libdir}/cairo-dock/libcd-powermanager.so

#---------------------------------------------------------------------
%package -n %{packagename}-shortcuts
Summary: That package provides a shortcuts plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}
Requires: %{packagename}-shared-images = %{version}

%description -n %{packagename}-shortcuts
An applets thatlet you acces quickly to all of your shortcuts.
It can manage disks, network points, and Nautilus bookmarks.
You can add or remove bookmarks bye drag'n'drop, even if you
don't have Nautilus. Middle-click to acces your desktop easily

%files -n %{packagename}-shortcuts
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/shortcuts
%{_libdir}/cairo-dock/libcd-shortcuts.so

#---------------------------------------------------------------------
%package -n %{packagename}-show_mouse
Summary: That package provides plugin "show_mouse"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-show_mouse
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %{packagename}-show_mouse
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/show_mouse
%{_libdir}/cairo-dock/libcd-show_mouse.so

#---------------------------------------------------------------------
%package -n %{packagename}-systray
Summary: That package provides a systray plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-systray
Add a systray to your dock!

%files -n %{packagename}-systray
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/systray
%{_libdir}/cairo-dock/libcd-systray.so

#---------------------------------------------------------------------
%package -n %{packagename}-toons
Summary: That package provides plugin "toons"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-toons
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %{packagename}-toons
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Toons
%{_libdir}/cairo-dock/libcd-Toons.so

#---------------------------------------------------------------------
%package -n %{packagename}-weather
Summary: That package provides a weather plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-weather
This applet displyas weather into your dock.
It can detach itself to be a ttally eye-candy 3D Desklet.
You can have many valuable info by (middle) clicking on
the icons. Data are provided by www.weather.com

%files -n %{packagename}-weather
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/weather
%{_libdir}/cairo-dock/libcd-weather.so

#---------------------------------------------------------------------
%package -n %{packagename}-xgamma
Summary: That package provides a Xgamma plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-xgamma
Setup the gama of your screen directly from the dock.
It is a simple port of xgamma. Quickly setup gamma with
left click, or more accurately with middle click.

%files -n %{packagename}-xgamma
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Xgamma
%{_libdir}/cairo-dock/libcd-Xgamma.so

#---------------------------------------------------------------------
%package -n %{packagename}-alsamixer
Summary: That package provides a alsaMixer plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-alsamixer
This applet let you set up the sound volume from the dock.
Click on icon to show/hide volume comtrol (You can bin a
keyboard shortcut for it.)
Middle-click to set or unset mute. This applet works with
the Alsa sound drivers.

%files -n %{packagename}-alsamixer
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/AlsaMixer
%{_libdir}/cairo-dock/libcd-AlsaMixer.so

#---------------------------------------------------------------------
%package -n %{packagename}-cairo-penguin
Summary: That package provides a Cairo-Penguin plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-cairo-penguin
Add a lively Penguin in your dock! Left click to change animation,
right click to disturb him ^_^.
Images are from Pingus, Inspiration is from xpenguins.

%files -n %{packagename}-cairo-penguin
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Cairo-Penguin
%{_libdir}/cairo-dock/libcd-Cairo-Penguin.so

#---------------------------------------------------------------------
%package -n %{packagename}-slider
Summary: That package provides a slider plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-slider
The slider applet is a basic image slider.

%files -n %{packagename}-slider
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/slider
%{_libdir}/cairo-dock/libcd-slider.so

#---------------------------------------------------------------------
%package -n %{packagename}-stack
Summary: That package provides a stack plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-stack
This applet allows you to build a stack of items, just like the Stack
applet of MacOS X. Items can be files, folders, URL, or even pieces of
text.

%files -n %{packagename}-stack
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/stack
%{_libdir}/cairo-dock/libcd-stack.so

#---------------------------------------------------------------------
%package -n %{packagename}-System-monitor
Summary: That package provides plugin "System-monitor"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}
Obsoletes: %{packagename}-rame < 2.1.2
Obsoletes: %{packagename}-cpusage < 2.1.2
Obsoletes: %{packagename}-nvidia < 2.1.2

%description -n %{packagename}-System-monitor
This applet shows you the CPU load, RAM usage, graphic card temperature, etc.
Middle click on the icon to get some valuable info.
Left click on the icon to get a list of the most ressources using programs.
You can instanciate this applet several times to show different values each time.

%files -n %{packagename}-System-monitor
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/System-monitor
%{_libdir}/cairo-dock/libcd-system-monitor.so

#---------------------------------------------------------------------
%package -n %{packagename}-wifi
Summary: That package provides a wifi plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-wifi
The wifi applet show you the signal strenght of
the first active connection.

%files -n %{packagename}-wifi
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/wifi
%{_libdir}/cairo-dock/libcd-wifi.so

#---------------------------------------------------------------------
%package -n %{packagename}-xfce-integration
Summary: That package provides a xfce-integration plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-xfce-integration
This applet provides functions for a better integration into XFCE.

%files -n %{packagename}-xfce-integration
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/xfce-integration
%{_libdir}/cairo-dock/libcd_xfce-integration.so

#---------------------------------------------------------------------
%package -n %{packagename}-tomboy
Summary: That package provides a tomboy plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-tomboy
Control your TomBoy's notes directly in the dock!

%files -n %{packagename}-tomboy
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/tomboy
%{_libdir}/cairo-dock/libcd-tomboy.so

#---------------------------------------------------------------------
%package -n %{packagename}-netspeed
Summary: That package provides a netspeed plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-netspeed
the netspeed applet show you the bit rate of your internet connection
and make some stats on it.

%files -n %{packagename}-netspeed
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/netspeed
%{_libdir}/cairo-dock/libcd-netspeed.so

#---------------------------------------------------------------------
%package -n %{packagename}-switcher
Summary: That package provides a switcher plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-switcher
The new and soon wonderful switcher applet

%files -n %{packagename}-switcher
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/switcher
%{_libdir}/cairo-dock/libcd-switcher.so

#---------------------------------------------------------------------
%package -n %{packagename}-dbus
Summary: That package provides a Dbus plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-dbus
This plug-in lets extern pllication interact on the dock.
The communication between both sides is based on Dbus.

%files -n %{packagename}-dbus
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Dbus
%{_libdir}/cairo-dock/libcd-Dbus.so

#---------------------------------------------------------------------
%if %mdkversion >= 201100
%package -n %{packagename}-recent-events
Summary:     Recent-Events applet based on Zeitgeist framework
Group:       Graphical desktop/Other
Requires:    %{name}-i18n = %{version}

%description -n %{packagename}-recent-events
This applet is an quite complex and Gnome Activity Journal like.
Features:
* you can browse recent tracked events by categories (All,
  Document, Folder, Image, Audioa, Video, Other, Top Results)
* you can look for events (search through it and delete the searched item)
* the tracked items have thumbnails
* huge list of recent items

%files -n %{packagename}-recent-events
%defattr(-, root, root)
%{_libdir}/cairo-dock/libcd-Recent-Events.so
%{_datadir}/cairo-dock/plug-ins/Recent-Events/*
%endif

#---------------------------------------------------------------------
%package -n %{packagename}-showdesktop
Summary: That package provides a showDesktop plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}
Requires: %{packagename}-shared-images = %{version}

%description -n %{packagename}-showdesktop
This applet let you acces quickly to your desktop.

%files -n %{packagename}-showdesktop
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/showDesktop
%{_libdir}/cairo-dock/libcd-showDesktop.so

#---------------------------------------------------------------------
%if %mdkversion > 200800
%package -n %{packagename}-gnome-integration
Summary: That package provides a gnome-integration plugins
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-gnome-integration
This applet provides functions for a better integration into GNOME.

%files -n %{packagename}-gnome-integration
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/gnome-integration
%{_libdir}/cairo-dock/libcd_gnome-integration.so
%endif

#---------------------------------------------------------------------
%package -n %{packagename}-clipper
Summary: That package provides plugin "clipper"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-clipper
This applet keeps a trace of the clipboard and mouse selection, so that
you can recall them quickly. It's a clone of the well-know Klipper.

%files -n %{packagename}-clipper
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Clipper
%{_libdir}/cairo-dock/libcd-Clipper.so

#---------------------------------------------------------------------
%package -n %{packagename}-keyboard-indicator
Summary: That package provides plugin "keyboard-indicator"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-keyboard-indicator
This applet lets you control the keyboard layout.

%files -n %{packagename}-keyboard-indicator
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/keyboard-indicator
%{_libdir}/cairo-dock/libcd-keyboard-indicator.so

#---------------------------------------------------------------------
%package -n %{packagename}-weblets
Summary: That package provides plugin "weblets"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-weblets
The weblets applet allows you to show an interactive web page on your desktop.

%files -n %{packagename}-weblets
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/weblets
%{_libdir}/cairo-dock/libcd-weblets.so

#---------------------------------------------------------------------
%package -n %{packagename}-rssreader
Summary: That package provides plugin "rssreader"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-rssreader
This applet is an RSS/Atom feed reader. You can instanciate it as many
times as you want.

%files -n %{packagename}-rssreader
%defattr(-, root, root)
%{_libdir}/cairo-dock/libcd-rssreader.so
%{_datadir}/cairo-dock/plug-ins/RSSreader

#---------------------------------------------------------------------
%package -n %{packagename}-Folders
Summary: That package provides plugin "Folders"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-Folders
This applet imports folders inside the Dock.

%files -n %{packagename}-Folders
%defattr(-, root, root)
%{_libdir}/cairo-dock/libcd-Folders.so
%{_datadir}/cairo-dock/plug-ins/Folders

#---------------------------------------------------------------------
%package -n %{packagename}-remote-control
Summary: That package provides plugin "remote-control"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-remote-control
This plug-in lets you control your dock from the keyboard or even
a remote controller.

%files -n %{packagename}-remote-control
%defattr(-, root, root)
%{_libdir}/cairo-dock/libcd-Remote-Control.so
%{_datadir}/cairo-dock/plug-ins/Remote-Control

#---------------------------------------------------------------------
%if %mdkversion >= 201100
%package -n %{packagename}-vala
Summary: This package provides vala binding for %{packagename}
Group: Graphical desktop/Other

%description -n %{packagename}-vala
This package provides vala binding for %{packagename}.

%files -n %{packagename}-vala
%defattr(-, root, root)
%{_libdir}/libCDApplet.so
%{_libdir}/pkgconfig/CDApplet.pc
%{_datadir}/vala*/vapi/CDApplet.*
%endif

#---------------------------------------------------------------------
%package -n %{packagename}-shared-images
Summary: Shared images for plugins
Group: Graphical desktop/Other

%description -n %{packagename}-shared-images
This package provides shared images for plugins.

%files -n %{packagename}-shared-images
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/shared-images

#---------------------------------------------------------------------
%package -n %{packagename}-composite-manager
Summary: That package provides plugin "composite-manager"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}
Requires: %{packagename}-shared-images = %{version}

%description -n %{packagename}-composite-manager
This applet allows you to toggle the composite ON/OFF.

%files -n %{packagename}-composite-manager
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Composite-Manager
%{_libdir}/cairo-dock/libcd-Composite-Manager.so
#---------------------------------------------------------------------

%package -n %{packagename}-status-notifier
Summary:    That package provides plugin "status-notifier"
Group:      Graphical desktop/Other
Requires:   %{name}-i18n = %{version}

%description -n %{packagename}-status-notifier
This package provides plugin Status Notifier for %{packagename}.

%files -n %{packagename}-status-notifier
%defattr(-, root, root)
%{_libdir}/cairo-dock/libcd-status-notifier.so
#%{_libdir}/cli/CDApplet.dll
%{ruby_libdir}/CDApplet.rb
%{_datadir}/cairo-dock/plug-ins/Status-Notifier
%{_libdir}/cairo-dock/status-notifier-watcher

#---------------------------------------------------------------------
%package -n %{packagename}-gmenu
Summary: That package provides plugin "gmenu"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-gmenu
The new and soon wonderful GMenu applet

%files -n %{packagename}-gmenu
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/GMenu
%{_libdir}/cairo-dock/libcd-GMenu.so
#---------------------------------------------------------------------
%package -n %{packagename}-impulse
Summary: That package provides plugin "impulse"
Group: Graphical desktop/Other
Requires: %{name}-i18n = %{version}

%description -n %{packagename}-impulse
Graphical equalizer in the dock depending on the signal given by PulseAudio.

%files -n %{packagename}-impulse
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Impulse
%{_libdir}/cairo-dock/libcd-Impulse.so
#---------------------------------------------------------------------


%prep
%setup -qn %{name}-%{version}~2

for i in */src/CMakeLists.txt
do
	sed -i -e 's/ SHARED/ MODULE /' $i
done

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
rm -f %{buildroot}/usr/lib/cli/CDApplet.dll

%find_lang %{name}

%clean
rm -rf %{buildroot}
