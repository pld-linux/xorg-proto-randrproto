Summary:	RandR extension headers
Summary(pl.UTF-8):	Nagłówki rozrzerzenia RandR
Name:		xorg-proto-randrproto
Version:	1.2.99.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/randrproto-%{version}.tar.bz2
# Source0-md5:	dba22f3a3791db31befec7a227c445a3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RandR extension headers.

The X Resize, Rotate and Reflect Extension, called RandR for short,
brings the ability to resize, rotate and reflect the root window of a
screen. It is based on the X Resize and Rotate Extension as specified
in the Proceedings of the 2001 Usenix Technical Conference [RANDR].

%description -l pl.UTF-8
Nagłówki rozszerzenia RandR.

Rozszerzenie X Resize, Rotate and Reflect (w skrócie RandR) daje
możliwość zmiany rozmiaru, obrotu i odbicia głównego okna ekranu. Jest
oparte na rozszerzeniu X Resize and Rotate opisanym w protokołach
konferencji 2001 Usenix Technical Conference [RANDR].

%package devel
Summary:	RandR extension headers
Summary(pl.UTF-8):	Nagłówki rozrzerzenia RandR
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	randrext

%description devel
RandR extension headers.

The X Resize, Rotate and Reflect Extension, called RandR for short,
brings the ability to resize, rotate and reflect the root window of a
screen. It is based on the X Resize and Rotate Extension as specified
in the Proceedings of the 2001 Usenix Technical Conference [RANDR].

%description devel -l pl.UTF-8
Nagłówki rozszerzenia RandR.

Rozszerzenie X Resize, Rotate and Reflect (w skrócie RandR) daje
możliwość zmiany rozmiaru, obrotu i odbicia głównego okna ekranu. Jest
oparte na rozszerzeniu X Resize and Rotate opisanym w protokołach
konferencji 2001 Usenix Technical Conference [RANDR].

%prep
%setup -q -n randrproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog randrproto.txt
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/randrproto.pc
