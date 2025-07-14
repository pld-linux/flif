#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	Free Lossless Image Format library
Summary(pl.UTF-8):	Biblioteka do obsługi formatu FLIF (Free Lossless Image Format)
Name:		flif
Version:	0.4
Release:	1
License:	LGPL v3+ (libflif and programs), Apache v2.0 (libflif_dec)
Group:		Libraries
#Source0Download: https://github.com/FLIF-hub/FLIF/releases
Source0:	https://github.com/FLIF-hub/FLIF/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c9615a4a525ecd39b27317ceb8365652
Patch0:		%{name}-install.patch
URL:		http://flif.info/
BuildRequires:	SDL2-devel >= 2
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gdk-pixbuf2-devel >= 2.10
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
FLIF is a lossless image format based on MANIAC compression. MANIAC
(Meta-Adaptive Near-zero Integer Arithmetic Coding) is a variant of
CABAC (context-adaptive binary arithmetic coding), where the contexts
are nodes of decision trees which are dynamically learned at encode
time.

FLIF outperforms PNG, FFV1, lossless WebP, lossless BPG and lossless
JPEG2000 in terms of compression ratio.

Moreover, FLIF supports a form of progressive interlacing (essentially
a generalization/improvement of PNG's Adam7).

%description -l pl.UTF-8
FLIF (Free Lossless Image Format - wolnodostępny, bezstratny format
obrazu) to bezstratny format obrazów oparty na kompresji MANIAC.
MANIAC (Meta-Adaptive Near-zero Integer Arithmetic Coding -
meta-adaptacyjne kodowanie arytmetyczne liczbami całkowitymi bliskimi
zeru) to wariant kompresji CABAC (kontekstowo-adaptacyjne binarne
kodowanie arytmetyczne), gdzie kontekstem są węzły drzew decyzyjnych,
dynamicznie wyuczanych w trakcie kodowania.

FLIF pod względem współczynnika kompresji jest wydajniejszy niż PNG,
FFV1, bezstratny WebP, bezstratny BPG i bezstratny JPEG2000.

Ponadto FLIF obsługuje rodzaj przeplotu progresywnego (zasadniczo
uogólnienie/rozwinięcie schematu Adam7 z PNG).

%package devel
Summary:	Header files for FLIF libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek FLIF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FLIF libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek FLIF.

%package static
Summary:	Static FLIF library
Summary(pl.UTF-8):	Statyczna biblioteka FLIF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FLIF library.

%description static -l pl.UTF-8
Statyczna biblioteka FLIF.

%package dec
Summary:	FLIF decoder library
Summary(pl.UTF-8):	Biblioteka dekodera FLIF
License:	Apache v2.0
Group:		Libraries

%description dec
FLIF decoder library.

%description dec -l pl.UTF-8
Biblioteka dekodera FLIF.

%package dec-devel
Summary:	Development files for FLIF decoder library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki dekodera FLIF
License:	Apache v2.0
Group:		Development/Libraries
Requires:	%{name}-dec = %{version}-%{release}
# for headers
Requires:	%{name}-devel = %{version}-%{release}

%description dec-devel
Development files for FLIF decoder library.

%description dec-devel -l pl.UTF-8
Pliki programistyczne biblioteki dekodera FLIF.

%package dec-static
Summary:	Static FLIF decoder library
Summary(pl.UTF-8):	Statyczna biblioteka dekodera FLIF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description dec-static
Static FLIF decoder library.

%description dec-static -l pl.UTF-8
Statyczna biblioteka dekodera FLIF.

%package tools
Summary:	Tools to convert from/to FLIF image format
Summary(pl.UTF-8):	Narzędzia do konwersji do/z formatu obrazów FLIF
License:	LGPL v3+
Group:		Applications/Graphics
Suggests:	ImageMagick >= 1:6.8
Suggests:	apngdis >= 2.5

%description tools
Tools to convert from/to FLIF image format.

%description tools -l pl.UTF-8
Narzędzia do konwersji do/z formatu obrazów FLIF.

%package view
Summary:	SDL2 based FLIF viewer
Summary(pl.UTF-8):	Przeglądarka plików FLIF oparta na bibliotece SDL2
License:	LGPL v3+
Group:		Applications/Graphics
Requires:	%{name}-dec = %{version}-%{release}

%description view
SDL2 based FLIF viewer.

%description view -l pl.UTF-8
Przeglądarka plików FLIF oparta na bibliotece SDL2.

%package -n bash-completion-flif
Summary:	Bash completion for flif command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia flif
Group:		Applications/Shells
Requires:	%{name}-tools = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-flif
Bash completion for flif command.

%description -n bash-completion-flif -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia flif.

%package -n gdk-pixbuf2-loader-flif
Summary:	FLIF loader module for gdk-pixbuf2 library
Summary(pl.UTF-8):	Moduł biblioteki gdk-pixbuf2 wczytujący pliki FLIF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2 >= 2.10
Requires:	shared-mime-info

%description -n gdk-pixbuf2-loader-flif
FLIF loader module for gdk-pixbuf2 library.

%description -n gdk-pixbuf2-loader-flif -l pl.UTF-8
Moduł biblioteki gdk-pixbuf2 wczytujący pliki FLIF.

%prep
%setup -q -n FLIF-%{version}
%patch -P0 -p1

%build
install -d src/build
cd src/build
%cmake .. \
	%{!?with_static_libs:-DBUILD_STATIC_LIBS=OFF}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src/build install \
	DESTDIR=$RPM_BUILD_ROOT

# already in file
%{__rm} $RPM_BUILD_ROOT%{_datadir}/FLIF/flif.magic

install -Dp doc/flif.bash-completion $RPM_BUILD_ROOT%{bash_compdir}/flif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	dec -p /sbin/ldconfig
%postun	dec -p /sbin/ldconfig

%post	-n gdk-pixbuf2-loader-flif
umask 022
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache || :
%update_mime_database

%postun	-n gdk-pixbuf2-loader-flif
%update_mime_database
if [ "$1" != "0" ]; then
	umask 022
	[ ! -x %{_bindir}/gdk-pixbuf-query-loaders%{pqext} ] || \
	%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache || :
fi

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libflif.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/metadata
%attr(755,root,root) %{_libdir}/libflif.so
%{_includedir}/flif*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libflif.a
%endif

%files dec
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflif_dec.so.0

%files dec-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflif_dec.so

%if %{with static_libs}
%files dec-static
%defattr(644,root,root,755)
%{_libdir}/libflif_dec.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apng2flif
%attr(755,root,root) %{_bindir}/dflif
%attr(755,root,root) %{_bindir}/flif
%attr(755,root,root) %{_bindir}/gif2flif
%{_mandir}/man1/flif.1*

%files view
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/viewflif

%files -n bash-completion-flif
%defattr(644,root,root,755)
%{bash_compdir}/flif

%files -n gdk-pixbuf2-loader-flif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-flif.so
%{_datadir}/mime/packages/flif-mime.xml
