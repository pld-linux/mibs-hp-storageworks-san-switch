Summary:	MIBs for HP StorageWorks SAN Switches v5.x firmware
Summary(pl.UTF-8):	MIB-y dla switchy SAN HP StorageWorks z firmware v5.x
Name:		mibs-hp-storageworks-san-switch
Version:	5.0.x
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	ftp://ftp.hp.com/pub/softlib/software6/COL13337/co-37211-1/v%{version}_mibs.zip
# Source0-md5:	9f85e4a28b988289ec26580c0fadade1
URL:		http://www.hp.com/rnd/software/MIBs.htm
BuildRequires:	unzip
Requires:	mibs-dirs
Obsoletes:	net-snmp-mibs-hp-storageworks-san-switch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/mibs

%description
MIBs for B-Series HP StorageWorks SAN Switches that run v5.x firmware.

%description -l pl.UTF-8
MIB-y dla switchy HP StorageWorks serii B z firmware w wersji 5.x.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a *.mib $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf
%{mibdir}/*
