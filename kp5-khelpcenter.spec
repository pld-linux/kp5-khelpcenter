%define		kdeplasmaver	5.5.4
%define		qtver		5.4.0
%define		kpname		khelpcenter
Summary:	khelpcenter
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	e47e2afb0bdef8733408467d24199694
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
khelpcenter

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khelpcenter
%{_libdir}/khc_docbookdig.pl
%{_libdir}/khc_htdig.pl
%{_libdir}/khc_htsearch.pl
%{_libdir}/khc_indexbuilder
%{_libdir}/khc_mansearch.pl
%attr(755,root,root) %{_libdir}/libkdeinit5_khelpcenter.so
%{_desktopdir}/org.kde.Help.desktop
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.khelpcenter.kcmhelpcenter.xml
%{_datadir}/kde4/services/khelpcenter.desktop
%{_datadir}/khelpcenter/glossary.html.in
%{_datadir}/khelpcenter/glossary.xslt
%{_datadir}/khelpcenter/index.html.in
%{_datadir}/khelpcenter/plugins/Applications/.directory
%{_datadir}/khelpcenter/plugins/Manpages/.directory
%{_datadir}/khelpcenter/plugins/Manpages/man1.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man2.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man3.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man4.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man5.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man6.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man7.desktop
%{_datadir}/khelpcenter/plugins/Manpages/man8.desktop
%{_datadir}/khelpcenter/plugins/Scrollkeeper/.directory
%{_datadir}/khelpcenter/plugins/Scrollkeeper/scrollkeeper.desktop
%{_datadir}/khelpcenter/plugins/browsercontrolmodules.desktop
%{_datadir}/khelpcenter/plugins/filemanagercontrolmodules.desktop
%{_datadir}/khelpcenter/plugins/fundamentals.desktop
%{_datadir}/khelpcenter/plugins/info.desktop
%{_datadir}/khelpcenter/plugins/kcontrolmodules.desktop
%{_datadir}/khelpcenter/plugins/kicmodules.desktop
%{_datadir}/khelpcenter/plugins/kioslaves.desktop
%{_datadir}/khelpcenter/plugins/konquerorcontrolmodules.desktop
%{_datadir}/khelpcenter/plugins/onlinehelp.desktop
%{_datadir}/khelpcenter/plugins/othercontrolmodules.desktop
%{_datadir}/khelpcenter/plugins/plasma.desktop
%{_datadir}/khelpcenter/searchhandlers/docbook.desktop
%{_datadir}/khelpcenter/searchhandlers/htdig.desktop
%{_datadir}/khelpcenter/searchhandlers/htdig/htdig_long.html
%{_datadir}/khelpcenter/searchhandlers/man.desktop
%{_datadir}/khelpcenter/table-of-contents.xslt
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/kxmlgui5/khelpcenter/khelpcenterui.rc
