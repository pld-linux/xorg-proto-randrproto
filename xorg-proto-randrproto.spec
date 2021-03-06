# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	RandR extension headers
Summary(pl.UTF-8):	Nagłówki rozrzerzenia RandR
Name:		xorg-proto-randrproto
Version:	1.5.0
Release:	1.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/randrproto-%{version}.tar.bz2
# Source0-md5:	a46765c8dcacb7114c821baf0df1e797
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README randrproto.txt
%{_includedir}/X11/extensions/randr*.h
%{_pkgconfigdir}/randrproto.pc
