Summary:	xvinfo application
Summary(pl):	Aplikacja xvinfo
Name:		xorg-app-xvinfo
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xvinfo-%{version}.tar.bz2
# Source0-md5:	e81bdb7f853f4a0a4d0bd0bb66bf3bff
Patch0:		xvinfo-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xvinfo application.

%description -l pl
Aplikacja xvinfo.

%prep
%setup -q -n xvinfo-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
