%define major		5
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d

Summary:	A frontend for MLDonkey
Name:		kmldonkey
Version:	2.0.7
Release:	4
License:	GPL
Group:		Graphical desktop/KDE
URL:		http://extragear.kde.org/apps/kmldonkey/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel
Requires:	mldonkey

%description
KMLDonkey is a frontend for MLDonkey, a powerful P2P file sharing tool,
designed for the KDE desktop.

%files
%{_kde_bindir}/kmldonkey
%{_kde_applicationsdir}/kmldonkey.desktop
%{_kde_appsdir}/kmldonkey/icons/hicolor/*/apps/*
%{_kde_appsdir}/kmldonkey/*rc
%{_kde_iconsdir}/hicolor/*/apps/*
%{_kde_services}/*-kmldonkey.desktop
%{_kde_libdir}/kde4/plasma_engine_kmldonkey.so
%{_kde_libdir}/kde4/plasma_applet_kmldonkey.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	KMLDonkey shared libraries
Group:		System/Libraries

%description -n %{libname}
Shared libraries needed by %{name}.

%files -n %{libname}
%{_kde_libdir}/*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the libraries and header files needed to
develop programs which make use of %{name}.

%files -n %{devname}
%{_kde_includedir}/kmldonkey
%{_kde_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

