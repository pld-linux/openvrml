%include	/usr/lib/rpm/macros.perl
Summary:	VRML97 runtime library.
Name:		openvrml
Version:	0.15.5
Release:	0.1
License:	LGPL
Group:		System Environment/Libraries
Source0:	http://dl.sourceforge.net/openvrml/%{name}-%{version}.tar.gz
# Source0-md5:	4d4a68af69c380cf4af22247c3a53215
URL:		http://www.openvrml.org/
BuildRequires:  pkgconfig >= 0.12.0
BuildRequires:  boost-devel >= 1.30.2
BuildRequires:  zlib-devel >= 1.1.3
BuildRequires:  libpng-devel >= 1.0.12
BuildRequires:  libjpeg-devel >= 6b
BuildRequires:  fontconfig-devel >= 2.0
BuildRequires:  freetype-devel >= 2.1.2
BuildRequires:  mozilla-devel >= 1.6
BuildRequires:  libgcj-devel >= 3.3
BuildRequires:  xorg-x11-devel >= 6.7
BuildRequires:  SDL-devel >= 1.2
BuildRequires:  dejagnu >= 1.4
BuildRequires:  gtk2-devel
Requires:       zlib >= 1.1.3
Requires:       libpng >= 1.0.12
Requires:       libjpeg >= 6b
Requires:       fontconfig >= 2.0
Requires:       freetype >= 2.1.2
Requires:       mozilla >= 1.6
Requires:       libgcj >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozilladir	/usr/%{_lib}/mozilla
%define		netscapedir	/usr/%{_lib}/netscape

#%define		_noautoreqdep	libGL.so.1 libGLU.so.1
# false positives found by perlreq from rpm 4.1
#%define		_noautoreq	'perl(VRML::Events)' 'perl(VRML::VRMLCU)' 'perl(VRML::VRMLFields)' 'perl(VRML::VRMLNodes)' 'perl(VRMLFields)' 'perl(VRMLNodes)' 'perl(VRMLRend)'

%description
OpenVRML is a free cross-platform runtime for VRML available under the
GNU Lesser General Public License. The basic OpenVRML distribution
includes libraries you can use to add VRML support to an application,
and Lookat, a simple stand-alone VRML browser.

%package devel
Summary:	Headers and static library for developing C++ programs with OpenVRML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers and static library that programmers will need to develop C++
programs using OpenVRML.

%package gl
Summary:	OpenGL renderer for OpenVRML
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-x11-Mesa-libGLU >= 6.7

%description gl
OpenGL renderer for OpenVRML.

%package gl-devel
Summary:	OpenVRML OpenGL renderer headers and static library.
Group:		Development/Libraries
Requires:	%{name}-gl = %{version}-%{release}
Requires:	xorg-x11-devel >= 6.7

%description gl-devel
Headers and static library that programmers will need to develop C++
programs using the OpenVRML OpenGL renderer.

%package -n lookat
Summary:	VRML viewer
Group:		Applications/Multimedia
Requires:	%{name}-gl = %{version}-%{release}
#Requires:	mozilla = %(rpm -q mozilla --qf='%%{epoch}:%%{version}')
Requires:	SDL >= 1.2

%description -n lookat
SDL-based VRML viewer.

%package -n mozilla-plugin-%{name}
Summary:	VRML plugin for Mozilla WWW browser
Summary(pl):	Wtyczka VRML dla przegl±darki WWW Mozilla
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mozilla-embedded(gtk2)

%description -n mozilla-plugin-%{name}
VRML plugin for Mozilla WWW browser.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka VRML dla przegl±darki WWW Mozilla.

%package -n netscape-plugin-%{name}
Summary:	VRML plugin for Netscape WWW browser
Summary(pl):	Wtyczka VRML dla przegl±darki WWW Netscape
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n netscape-plugin-%{name}
VRML plugin for Netscape WWW browser.

%description -n netscape-plugin-%{name} -l pl
Wtyczka VRML dla przegl±darki WWW Netscape.

%package -n mozilla-firefox-plugin-%{name}
Summary:	VRML plugin for Mozilla Firefox browser
Summary(pl):	Wtyczka VRML dla przegl±darki Mozilla Firefox
Group:		Libraries
PreReq:		mozilla-firefox
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-firefox-plugin-%{name}
VRML plugin for Mozilla Firefox browser.

%description -n mozilla-firefox-plugin-%{name} -l pl
Wtyczka VRML dla przegl±darki Mozilla Firefox.

%package -n konqueror-plugin-%{name}
Summary:	VRML plugin for Konqueror browser
Summary(pl):	Wtyczka VRML dla przegl±darki Konqueror
Group:		Libraries
PreReq:		konqueror >= 3.0.8-2.3
Requires:	%{name} = %{version}-%{release}

%description -n konqueror-plugin-%{name}
VRML plugin for Konqueror browser.

%description -n konqueror-plugin-%{name} -l pl
Wtyczka VRML dla przegl±darki Konqueror.

%prep
%setup -q
#%setup -q -n FreeWRL-%{version}
#%patch0 -p1
#%patch1 -p1
# for mozilla plugin - removed intentionaly?
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1

%build
%configure \
	CPPFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{mozilladir}/{plugins,java/classes},%{netscapedir}/plugins} \
	$RPM_BUILD_ROOT%{_libdir}/{mozilla-firefox/plugins,/kde3/plugins/konqueror}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.LESSER ChangeLog NEWS README THANKS
%{_libdir}/libopenvrml.so.*
%{_datadir}/openvrml/java/script.jar

%files devel
%doc doc/manual
%{_includedir}/%{name}/openvrml/*.h
%{_libdir}/libopenvrml.la
%{_libdir}/libopenvrml.a
%{_libdir}/libopenvrml.so
%{_libdir}/pkgconfig/openvrml.pc

%files gl
%{_libdir}/libopenvrml-gl.so.*

%files gl-devel
%{_includedir}/%{name}/openvrml/gl
%{_libdir}/libopenvrml-gl.la
%{_libdir}/libopenvrml-gl.a
%{_libdir}/libopenvrml-gl.so
%{_libdir}/pkgconfig/openvrml-gl.pc

%files -n lookat
%{_bindir}/lookat
%{_datadir}/pixmaps/lookat.xpm

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{mozilladir}/plugins/*.so

%files -n netscape-plugin-%{name}
%defattr(644,root,root,755)
%{netscapedir}/java/classes/*.jar
%attr(755,root,root) %{netscapedir}/plugins/*.so

%files -n mozilla-firefox-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla-firefox/plugins/*.so

%files -n konqueror-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/konqueror/*.so
