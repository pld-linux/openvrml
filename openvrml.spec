# TODO
# - doesn't build with mozilla-1.8-0.a6.2, 1.7.6-2.2 is fine
# - includedir/openvrml/openvrml sees like a bug
# - -devel deps
Summary:	VRML97 runtime library
Summary(pl.UTF-8):   Biblioteka uruchomieniowa VRML97
Name:		openvrml
Version:	0.15.9
Release:	0.5
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/openvrml/%{name}-%{version}.tar.gz
# Source0-md5:	a4134d658685be71596c620169221e6f
URL:		http://www.openvrml.org/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	X11-devel >= 1:6.7
BuildRequires:	boost-conversion-devel >= 1.30.2
BuildRequires:	boost-spirit-devel >= 1.30.2
BuildRequires:	boost-test-devel >= 1.30.2
BuildRequires:	dejagnu >= 1.4
BuildRequires:	fontconfig-devel >= 2.0
BuildRequires:	freetype-devel >= 2.1.2
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgcj-devel >= 5:3.3
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.12
BuildRequires:	mozilla-devel >= 5:1.7.6-2.2
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	zlib-devel >= 1.1.3
Requires:	fontconfig >= 2.0
Requires:	freetype >= 2.1.2
Requires:	libgcj >= 5:3.3
Requires:	libjpeg >= 6b
Requires:	libpng >= 1.0.12
Requires:	mozilla >= 5:1.7.6
Requires:	zlib >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenVRML is a free cross-platform runtime for VRML available under the
GNU Lesser General Public License. The basic OpenVRML distribution
includes libraries you can use to add VRML support to an application,
and Lookat, a simple stand-alone VRML browser.

%description -l pl.UTF-8
OpenVRML to wolnodostępne, wieloplatformowe środowisko uruchomieniowe
dla VRML dostępne na licencji GNU LGPL. Podstawowa dystrybucja
OpenVRML zawiera biblioteki, które można używać w celu dodania do
aplikacji obsługi VRML oraz Lookat - prostą, samodzielną przeglądarkę
VRML.

%package devel
Summary:	Headers for developing C++ programs with OpenVRML
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia programów w C++ z użyciem OpenVRML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers that programmers will need to develop C++ programs using
OpenVRML.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne programistom do tworzenia programów w C++
przy użyciu OpenVRML.

%package static
Summary:	Static OpenVRML library
Summary(pl.UTF-8):   Statyczna biblioteka OpenVRML
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenVRML library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenVRML.

%package gl
Summary:	OpenGL renderer for OpenVRML
Summary(pl.UTF-8):   Renderer OpenGL dla OpenVRML
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	X11-OpenGL-libs >= 1:6.7

%description gl
OpenGL renderer for OpenVRML.

%description gl -l pl.UTF-8
Renderer OpenGL dla OpenVRML.

%package gl-devel
Summary:	Header files for OpenVRML OpenGL renderer
Summary(pl.UTF-8):   Pliki nagłówkowe dla renderera OpenGL dla OpenVRML
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gl = %{version}-%{release}
Requires:	X11-devel >= 1:6.7.0

%description gl-devel
Headers that programmers will need to develop C++ programs using the
OpenVRML OpenGL renderer.

%description gl-devel -l pl.UTF-8
Pliki nagłówkowe potrzebne programistom do tworzenia programów w C++
przy użyciu renderera OpenGL dla OpenVRML.

%package gl-static
Summary:	Static OpenVRML OpenGL renderer library
Summary(pl.UTF-8):   Statyczna biblioteka renderera OpenGL dla OpenVRML
Group:		Development/Libraries
Requires:	%{name}-gl-devel = %{version}-%{release}

%description gl-static
Static OpenVRML OpenGL renderer library.

%description gl-static -l pl.UTF-8
Statyczna biblioteka renderera OpenGL dla OpenVRML.

%package -n lookat
Summary:	VRML viewer
Summary(pl.UTF-8):   Przeglądarka VRML
Group:		Applications/Multimedia
Requires:	%{name}-gl = %{version}-%{release}
#Requires:	mozilla = %(rpm -q mozilla --qf='%%{epoch}:%%{version}')
Requires:	SDL >= 1.2

%description -n lookat
SDL-based VRML viewer.

%description -n lookat -l pl.UTF-8
Przeglądarka VRML oparta na SDL.

%package -n mozilla-plugin-%{name}
Summary:	VRML plugin for Mozilla WWW browser
Summary(pl.UTF-8):   Wtyczka VRML dla przeglądarki WWW Mozilla
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mozilla-embedded(gtk2)

%description -n mozilla-plugin-%{name}
VRML plugin for Mozilla WWW browser.

%description -n mozilla-plugin-%{name} -l pl.UTF-8
Wtyczka VRML dla przeglądarki WWW Mozilla.

%package -n netscape-plugin-%{name}
Summary:	VRML plugin for Netscape WWW browser
Summary(pl.UTF-8):   Wtyczka VRML dla przeglądarki WWW Netscape
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n netscape-plugin-%{name}
VRML plugin for Netscape WWW browser.

%description -n netscape-plugin-%{name} -l pl.UTF-8
Wtyczka VRML dla przeglądarki WWW Netscape.

%package -n mozilla-firefox-plugin-%{name}
Summary:	VRML plugin for Mozilla Firefox browser
Summary(pl.UTF-8):   Wtyczka VRML dla przeglądarki Mozilla Firefox
Group:		Libraries
PreReq:		mozilla-firefox
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-firefox-plugin-%{name}
VRML plugin for Mozilla Firefox browser.

%description -n mozilla-firefox-plugin-%{name} -l pl.UTF-8
Wtyczka VRML dla przeglądarki Mozilla Firefox.

%package -n konqueror-plugin-%{name}
Summary:	VRML plugin for Konqueror browser
Summary(pl.UTF-8):   Wtyczka VRML dla przeglądarki Konqueror
Group:		Libraries
PreReq:		konqueror >= 3.0.8-2.3
Requires:	%{name} = %{version}-%{release}

%description -n konqueror-plugin-%{name}
VRML plugin for Konqueror browser.

%description -n konqueror-plugin-%{name} -l pl.UTF-8
Wtyczka VRML dla przeglądarki Konqueror.

%prep
%setup -q

%build
%configure \
	CPPFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}" \
	XPIDL=%{_bindir}/xpidl \
	XPIDLFLAGS="-I %{_datadir}/idl" \
	mozincludedir=%{_includedir}/mozilla

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/{mozilla{,-firefox},netscape,kde3}/plugins/konqueror

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mozilla-firefox
install $RPM_BUILD_ROOT%{_libdir}/mozilla{/plugins/openvrml.{so,xpt},-firefox/plugins}
# kde
install $RPM_BUILD_ROOT%{_libdir}/{mozilla/plugins,kde3/plugins/konqueror}/openvrml.so
# netscape
install $RPM_BUILD_ROOT%{_libdir}/{mozilla,netscape}/plugins/openvrml.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gl -p /sbin/ldconfig
%postun	gl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.LESSER ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/libopenvrml.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/manual
%attr(755,root,root) %{_libdir}/libopenvrml.so
%{_libdir}/libopenvrml.la
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/openvrml
%{_includedir}/%{name}/openvrml/*.h
%{_pkgconfigdir}/openvrml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenvrml.a

%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenvrml-gl.so.*.*.*

%files gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenvrml-gl.so
%{_libdir}/libopenvrml-gl.la
%{_includedir}/%{name}/openvrml/gl
%{_pkgconfigdir}/openvrml-gl.pc

%files gl-static
%defattr(644,root,root,755)
%{_libdir}/libopenvrml-gl.a

%files -n lookat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lookat
%{_pixmapsdir}/lookat.xpm

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_libdir}/mozilla/plugins/*.xpt
# dunno
%attr(755,root,root) %{_libdir}/openvrml-player
%{_datadir}/idl/%{name}-%{version}

%files -n netscape-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/netscape/plugins/*.so

%files -n mozilla-firefox-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla-firefox/plugins/*.so
%{_libdir}/mozilla-firefox/plugins/*.xpt

%files -n konqueror-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/konqueror/*.so
