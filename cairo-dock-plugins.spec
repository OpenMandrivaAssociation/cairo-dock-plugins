%define packagename cairo-dock

Summary:	Plugins for cairo-dock
Name:     	cairo-dock-plugins
Version:	1.6.3.1
Release:	%mkrel 1
License:	GPLv3+
Group:		Graphical desktop/Other
Source0: 	http://download.berlios.de/cairo-dock/%name-%version.tar.bz2
URL:		http://www.cairo-dock.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cairo-dock >= %version
BuildRequires:	cairo-dock-devel >= %version
BuildRequires:	glib2-devel
BuildRequires:	vte-devel
BuildRequires:	libalsa-devel
BuildRequires:	thunar-devel
BuildRequires:	intltool
BuildRequires:	gnutls-devel
BuildRequires:	gnome-menus-devel
Requires:	%{packagename}-clock
Requires:	%{packagename}-dustbin
Requires:	%{packagename}-logout
Requires:	%{packagename}-rendering
Requires:	%{packagename}-rhythmbox
Requires:	%{packagename}-terminal
Requires:	%{packagename}-powermanager
Requires:	%{packagename}-shortcuts
Requires:	%{packagename}-systray
Requires:	%{packagename}-weather
Requires:	%{packagename}-xgamma
Requires:	%{packagename}-alsamixer
Requires:	%{packagename}-cairo-penguin
Requires:	%{packagename}-tomboy
Requires:	%{packagename}-showdesklets
Requires:	%{packagename}-wifi
Requires:	%{packagename}-xmms
Requires:	%{packagename}-netspeed
Requires:	%{packagename}-rame
Requires:	%{packagename}-switcher
Requires:	%{packagename}-dbus
Requires:	%{packagename}-compiz-icon
Requires:	%{packagename}-showdesktop
Requires:	%{packagename}-slider
Requires:	%{packagename}-stack
Requires:	%{packagename}-cpusage
Requires:	%{packagename}-nvidia
Requires:	%{packagename}-clipper
Requires:	%{packagename}-gmenu

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package contains various plugins for cairo-dock.

%files
%defattr(-, root, root)

#---------------------------------------------------------------------
%package -n %{packagename}-clock
Summary: That package provides plugin "clock"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-clock
Display rime and date in your dock with the clock applet!
2 view are available: numeric and analogic.
It can derach itself to be the perfect clone of CairoClock.
It can warn you with alarms, can display a calendar, and
allow you to setup time and date.

%files -n %{packagename}-clock -f cd-clock.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/clock
%{_libdir}/cairo-dock/libcd-clock.so

#---------------------------------------------------------------------
%package -n %{packagename}-dustbin
Summary: That package provides plugin "dustbin"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-dustbin
Manage your disks space with this trash applet!
It can handle several trash directories,
threw files or unmount diisks with drag'n'drop,
warn you if you use too much space,
and display usefull info about your dustbins.

%files -n %{packagename}-dustbin -f cd-dustbin.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/dustbin
%{_libdir}/cairo-dock/libcd-dustbin.so

#---------------------------------------------------------------------
%package -n %{packagename}-logout
Summary: That package provides plugin "logout"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-logout
A very simple applet that adds an icon to log out
from your session.

%files -n %{packagename}-logout -f cd-logout.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/logout
%{_libdir}/cairo-dock/libcd-logout.so

#---------------------------------------------------------------------
%package -n %{packagename}-rendering
Summary: That package provides plugin "rendering"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-rendering
This module adds different views to your dock.
Any dock or sub-dock can be displayed with the
view of your choice. Currently, 3D-plane, Caroussel,
Parabolic and Rainbow views are provided

%files -n %{packagename}-rendering -f cd-rendering.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/rendering
%{_libdir}/cairo-dock/libcd-rendering.so

#---------------------------------------------------------------------
%package -n %{packagename}-rhythmbox
Summary: That package provides plugin "rhythmbox"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-rhythmbox
Control your Rhythmbox player directly in the dock!
Play/pause with left click, next song with middle click.

%files -n %{packagename}-rhythmbox -f cd-rhythmbox.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/rhythmbox
%{_libdir}/cairo-dock/libcd-rhythmbox.so

#---------------------------------------------------------------------
%package -n %{packagename}-terminal
Summary: That package provides plugin "terminal"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-terminal
Add a terminal to your dock!
You can drag'n'drop files or text into it
and select an action

%files -n %{packagename}-terminal -f cd-terminal.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/terminal
%{_libdir}/cairo-dock/libcd-terminal.so

#---------------------------------------------------------------------
%package -n %{packagename}-powermanager
Summary: That package provides a powermanager plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-powermanager
A power manager for laptop's battery
It works with ACPI and DBus.

%files -n %{packagename}-powermanager -f cd-powermanager.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/powermanager
%{_libdir}/cairo-dock/libcd-powermanager.so

#---------------------------------------------------------------------
%package -n %{packagename}-shortcuts
Summary: That package provides a shortcuts plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-shortcuts
An applets thatlet you acces quickly to all of your shortcuts.
It can manage disks, network points, and Nautilus bookmarks.
You can add or remove bookmarks bye drag'n'drop, even if you
don't have Nautilus. Middle-click to acces your desktop easily

%files -n %{packagename}-shortcuts -f cd-shortcuts.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/shortcuts
%{_libdir}/cairo-dock/libcd-shortcuts.so

#---------------------------------------------------------------------
%package -n %{packagename}-systray
Summary: That package provides a systray plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-systray
Add a systray to your dock!

%files -n %{packagename}-systray -f cd-systray.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/systray
%{_libdir}/cairo-dock/libcd-systray.so

#---------------------------------------------------------------------
%package -n %{packagename}-weather
Summary: That package provides a weather plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-weather
This applet displyas weather into your dock.
It can detach itself to be a ttally eye-candy 3D Desklet.
You can have many valuable info by (middle) clicking on
the icons. Data are provided by www.weather.com

%files -n %{packagename}-weather -f cd-weather.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/weather
%{_libdir}/cairo-dock/libcd-weather.so

#---------------------------------------------------------------------
%package -n %{packagename}-xgamma
Summary: That package provides a Xgamma plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-xgamma
Setup the gama of your screen directly from the dock.
It is a simple port of xgamma. Quickly setup gamma with
left click, or more accurately with middle click.

%files -n %{packagename}-xgamma -f cd-Xgamma.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Xgamma
%{_libdir}/cairo-dock/libcd-Xgamma.so

#---------------------------------------------------------------------
%package -n %{packagename}-alsamixer
Summary: That package provides a alsaMixer plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-alsamixer
This applet let you set up the sound volume from the dock.
Click on icon to show/hide volume comtrol (You can bin a
keyboard shortcut for it.)
Middle-click to set or unset mute. This applet works with
the Alsa sound drivers.

%files -n %{packagename}-alsamixer -f cd-AlsaMixer.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/AlsaMixer
%{_libdir}/cairo-dock/libcd-AlsaMixer.so

#---------------------------------------------------------------------
%package -n %{packagename}-cairo-penguin
Summary: That package provides a Cairo-Penguin plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-cairo-penguin
Add a lively Penguin in your dock! Left click to change animation,
right click to disturb him ^_^.
Images are from Pingus, Inspiration is from xpenguins.

%files -n %{packagename}-cairo-penguin -f cd-Cairo-Penguin.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Cairo-Penguin
%{_libdir}/cairo-dock/libcd-Cairo-Penguin.so

#---------------------------------------------------------------------
%package -n %{packagename}-showdesklets
Summary: That package provides a showDesklets plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-showdesklets
This applet let you acces quickly to your desklets.
Left click to show/hide your desklets.
Basically, if you are under Compiz, you don't need this applet;
you should just use the "Widgets Layer" copabilities of desklets.

%files -n %{packagename}-showdesklets -f cd-showDesklets.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/showDesklets
%{_libdir}/cairo-dock/libcd-showDesklets.so

#---------------------------------------------------------------------
%package -n %{packagename}-slider
Summary: That package provides a slider plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-slider
The slider applet is a basic image slider.

%files -n %{packagename}-slider -f cd-slider.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/slider
%{_libdir}/cairo-dock/libcd-slider.so

#---------------------------------------------------------------------
%package -n %{packagename}-stack
Summary: That package provides a stack plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-stack
This applet allows you to build a stack of items, just like the Stack
applet of MacOS X. Items can be files, folders, URL, or even pieces of
text.

%files -n %{packagename}-stack -f cd-stack.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/stack
%{_libdir}/cairo-dock/libcd-stack.so

#---------------------------------------------------------------------
%package -n %{packagename}-wifi
Summary: That package provides a wifi plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-wifi
The wifi applet show you the signal strenght of
the first active connection.

%files -n %{packagename}-wifi -f cd-wifi.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/wifi
%{_libdir}/cairo-dock/libcd-wifi.so

#---------------------------------------------------------------------
%package -n %{packagename}-xmms
Summary: That package provides a xmms plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-xmms
An applet dedicated to control XMMS, Audacious, Banshee & Exaile.
Keep in mind that only XMMS & Audacious are fully supported.
For XMMS you need to install 'xmms-infopipe' plug-in.
You can Drag&Drop sonng to put them in the queue.

%files -n %{packagename}-xmms -f cd-xmms.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/xmms
%{_libdir}/cairo-dock/libcd-xmms.so

#---------------------------------------------------------------------
%package -n %{packagename}-xfce-integration
Summary: That package provides a xfce-integration plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-xfce-integration
This applet provides functions for a better integration into XFCE.

%files -n %{packagename}-xfce-integration
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/xfce-integration
%{_libdir}/cairo-dock/libcd-xfce-integration.so

#---------------------------------------------------------------------
%package -n %{packagename}-tomboy
Summary: That package provides a tomboy plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-tomboy
Control your TomBoy's notes directly in the dock!

%files -n %{packagename}-tomboy -f cd-tomboy.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/tomboy
%{_libdir}/cairo-dock/libcd-tomboy.so

#---------------------------------------------------------------------
%package -n %{packagename}-netspeed
Summary: That package provides a netspeed plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-netspeed
the netspeed applet show you the bit rate of your internet connection
and make some stats on it.

%files -n %{packagename}-netspeed -f cd-netspeed.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/netspeed
%{_libdir}/cairo-dock/libcd-netspeed.so

#---------------------------------------------------------------------
%package -n %{packagename}-rame
Summary: That package provides a rame plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-rame
The rame applet show you the mount of RAM and SWAP
that is currently used

%files -n %{packagename}-rame -f cd-rame.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/rame
%{_libdir}/cairo-dock/libcd-rame.so

#---------------------------------------------------------------------
%package -n %{packagename}-switcher
Summary: That package provides a switcher plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-switcher
The new and soon wonderful switcher applet

%files -n %{packagename}-switcher -f cd-switcher.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/switcher
%{_libdir}/cairo-dock/libcd-switcher.so

#---------------------------------------------------------------------
%package -n %{packagename}-dbus
Summary: That package provides a Dbus plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-dbus
This plug-in lets extern pllication interact on the dock.
The communication between both sides is based on Dbus.

%files -n %{packagename}-dbus -f cd-Dbus.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Dbus
%{_libdir}/cairo-dock/libcd-Dbus.so

#---------------------------------------------------------------------
%package -n %{packagename}-compiz-icon
Summary: That package provides a Compiz-Icon plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-compiz-icon
The compiz-icon applet allow you to menage compiz and oher
windows manager. The sub-dock gives you acces to CCSM, Emerld
and some basic Compiz actions.

%files -n %{packagename}-compiz-icon -f cd-compiz-icon.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/compiz-icon
%{_libdir}/cairo-dock/libcd-compiz-icon.so

#---------------------------------------------------------------------
%package -n %{packagename}-showdesktop
Summary: That package provides a showDesktop plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-showdesktop
This applet let you acces quickly to your desktop.

%files -n %{packagename}-showdesktop -f cd-showDesktop.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/showDesktop
%{_libdir}/cairo-dock/libcd-showDesktop.so

#---------------------------------------------------------------------
%package -n %{packagename}-cpusage
Summary: That package provides a cpusage plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-cpusage
The cpusage applet show you the mount of CPU that is currently used.

%files -n %{packagename}-cpusage -f cd-cpusage.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/cpusage
%{_libdir}/cairo-dock/libcd-cpusage.so

#---------------------------------------------------------------------
%if %mdkversion > 200800
%package -n %{packagename}-gnome-integration
Summary: That package provides a gnome-integration plugins
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-gnome-integration
This applet provides functions for a better integration into GNOME.

%files -n %{packagename}-gnome-integration
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/gnome-integration
%{_libdir}/cairo-dock/libcd-gnome-integration.so
%endif

#---------------------------------------------------------------------
%package -n %{packagename}-nvidia
Summary: That package provides plugin "nVidia"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-nvidia
Manage your nVidia graphic card, check
your GPU temp and everything else.

%files -n %{packagename}-nvidia -f cd-nVidia.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/nVidia
%{_libdir}/cairo-dock/libcd-nVidia.so

#---------------------------------------------------------------------
%package -n %{packagename}-clipper
Summary: That package provides plugin "clipper"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-clipper
This applet keeps a trace of the clipboard and mouse selection, so that
you can recall them quickly. It's a clone of the well-know Klipper.

%files -n %{packagename}-clipper -f cd-Clipper.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/Clipper
%{_libdir}/cairo-dock/libcd-Clipper.so

#---------------------------------------------------------------------
%package -n %{packagename}-gmenu
Summary: That package provides plugin "gmenu"
Group: Graphical desktop/Other
Requires: %{packagename} = %{version}

%description -n %{packagename}-gmenu
The new and soon wonderful GMenu applet

%files -n %{packagename}-gmenu -f cd-GMenu.lang
%defattr(-, root, root)
%{_datadir}/cairo-dock/plug-ins/GMenu
%{_libdir}/cairo-dock/libcd-GMenu.so

#---------------------------------------------------------------------
%prep
%setup -q

%build
%configure2_5x \
  --disable-old-gnome-integration \
  --enable-gnome-integration \
  --enable-xfce-integration \
  --enable-alsa-mixer \
  --enable-terminal \
  --enable-gio-in-gmenu
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f %buildroot%{_libdir}/cairo-dock/libcd-*.la

%find_lang cd-AlsaMixer
%find_lang cd-Cairo-Penguin
%find_lang cd-Clipper
%find_lang cd-Dbus
%find_lang cd-GMenu
%find_lang cd-Xgamma
%find_lang cd-clock
%find_lang cd-compiz-icon
%find_lang cd-cpusage
%find_lang cd-dustbin
%find_lang cd-logout
%find_lang cd-nVidia
%find_lang cd-netspeed
%find_lang cd-powermanager
%find_lang cd-rame
%find_lang cd-rendering
%find_lang cd-rhythmbox
%find_lang cd-shortcuts
%find_lang cd-showDesklets
%find_lang cd-showDesktop
%find_lang cd-slider
%find_lang cd-stack
%find_lang cd-switcher
%find_lang cd-systray
%find_lang cd-terminal
%find_lang cd-tomboy
%find_lang cd-weather
%find_lang cd-wifi
%find_lang cd-xmms

%clean
rm -rf $RPM_BUILD_ROOT
