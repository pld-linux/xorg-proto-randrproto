Summary:	Randr protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Randr i pomocnicze
Name:		xorg-proto-randrproto
Version:	1.1.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/randrproto-X11R7.0-%{version}.tar.bz2
# Source0-md5:	bcf36d524f6f50aa16ee8e183350f7b8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Randr protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Randr i pomocnicze.

%package devel
Summary:	Randr protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Randr i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	randrext

%description devel
Randr protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Randr i pomocnicze.

%prep
%setup -q -n randrproto-X11R7.0-%{version}

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/randrproto.pc
