# TODO, need older mozilla than mozilla-1.8-0.a6.2?
# ./xpcom/components/nsIServiceManagerUtils.h seems available from mozilla-1.7.6
#openvrml.cpp:34:37: nsIServiceManagerUtils.h: No such file or
#directory
#openvrml.cpp:38:27: nsIDOMWindow.h: No such file or directory
#openvrml.cpp: In function `NPError NP_Initialize(NPNetscapeFuncs*,
#   NPPluginFuncs*)':
#openvrml.cpp:215: error: `do_GetService' undeclared (first use this
#function)
#openvrml.cpp:215: error: (Each undeclared identifier is reported only
#once for
#   each function it appears in.)
#make[2]: *** [openvrml.lo] Error 1
#make[2]: Leaving directory
#`/home/builder/rpm/BUILD/openvrml-0.15.5/mozilla-plugin/src'
Summary:	VRML97 runtime library.
Name:		openvrml
Version:	0.15.5
Release:	0.1
License:	LGPL
Group:		System Environment/Libraries
######		Unknown group!
Source0:	http://dl.sourceforge.net/openvrml/%{name}-%{version}.tar.gz
# Source0-md5:	4d4a68af69c380cf4af22247c3a53215
URL:		http://www.openvrml.org/
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	boost-devel >= 1.30.2
BuildRequires:	boost-conversion-devel >= 1.30.2
BuildRequires:	boost-spirit-devel >= 1.30.2
BuildRequires:	zlib-devel >= 1.1.3
BuildRequires:	libpng-devel >= 1.0.12
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	fontconfig-devel >= 2.0
BuildRequires:	freetype-devel >= 2.1.2
BuildRequires:	mozilla-devel >= 1.6
BuildRequires:	libgcj-devel >= 3.3
BuildRequires:	X11-devel >= 6.7
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	dejagnu >= 1.4
BuildRequires:	gtk+2-devel
Requires:	zlib >= 1.1.3
Requires:	libpng >= 1.0.12
Requires:	libjpeg >= 6b
Requires:	fontconfig >= 2.0
Requires:	freetype >= 2.1.2
Requires:	mozilla >= 1.6
Requires:	libgcj >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
######		Unknown group!
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
Summary(pl):	Wtyczka VRML dla przeglądarki WWW Mozilla
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mozilla-embedded(gtk2)

%description -n mozilla-plugin-%{name}
VRML plugin for Mozilla WWW browser.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka VRML dla przeglądarki WWW Mozilla.

%package -n netscape-plugin-%{name}
Summary:	VRML plugin for Netscape WWW browser
Summary(pl):	Wtyczka VRML dla przeglądarki WWW Netscape
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n netscape-plugin-%{name}
VRML plugin for Netscape WWW browser.

%description -n netscape-plugin-%{name} -l pl
Wtyczka VRML dla przeglądarki WWW Netscape.

%package -n mozilla-firefox-plugin-%{name}
Summary:	VRML plugin for Mozilla Firefox browser
Summary(pl):	Wtyczka VRML dla przeglądarki Mozilla Firefox
Group:		Libraries
PreReq:		mozilla-firefox
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-firefox-plugin-%{name}
VRML plugin for Mozilla Firefox browser.

%description -n mozilla-firefox-plugin-%{name} -l pl
Wtyczka VRML dla przeglądarki Mozilla Firefox.

%package -n konqueror-plugin-%{name}
Summary:	VRML plugin for Konqueror browser
Summary(pl):	Wtyczka VRML dla przeglądarki Konqueror
Group:		Libraries
PreReq:		konqueror >= 3.0.8-2.3
Requires:	%{name} = %{version}-%{release}

%description -n konqueror-plugin-%{name}
VRML plugin for Konqueror browser.

%description -n konqueror-plugin-%{name} -l pl
Wtyczka VRML dla przeglądarki Konqueror.

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
	CPPFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}" \
	XPIDL=%{_bindir}/xpidl

%{__make} \
	XPIDLFLAGS="-I %{_datadir}/idl" \
	mozincludedir=%{_includedir}/mozilla

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/{mozilla{,-firefox},netscape,kde3}/{plugins/konqueror,java/classes} \

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.LESSER ChangeLog NEWS README THANKS
%{_libdir}/libopenvrml.so.*
%{_datadir}/openvrml/java/script.jar

%files devel
%defattr(644,root,root,755)
%doc doc/manual
%{_includedir}/%{name}/openvrml/*.h
%{_libdir}/libopenvrml.la
%{_libdir}/libopenvrml.a
%attr(755,root,root) %{_libdir}/libopenvrml.so
%{_libdir}/pkgconfig/openvrml.pc

%files gl
%defattr(644,root,root,755)
%{_libdir}/libopenvrml-gl.so.*

%files gl-devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/openvrml/gl
%{_libdir}/libopenvrml-gl.la
%{_libdir}/libopenvrml-gl.a
%attr(755,root,root) %{_libdir}/libopenvrml-gl.so
%{_libdir}/pkgconfig/openvrml-gl.pc

%files -n lookat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lookat
%{_datadir}/pixmaps/lookat.xpm

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so

%files -n netscape-plugin-%{name}
%defattr(644,root,root,755)
%{_libdir}/netscape/java/classes/*.jar
%attr(755,root,root) %{_libdir}/netscape/plugins/*.so

%files -n mozilla-firefox-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla-firefox/plugins/*.so

%files -n konqueror-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/konqueror/*.so
