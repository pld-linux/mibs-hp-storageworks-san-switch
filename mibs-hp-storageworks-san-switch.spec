Summary:	MIBs for HP StorageWorks SAN Switches v5.x firmware
Summary(pl.UTF-8):	MIB-y dla switchy SAN HP StorageWorks z firmware v5.x
Name:		net-snmp-mibs-hp-storageworks-san-switch
Version:	5.0.x
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	ftp://ftp.hp.com/pub/softlib/software6/COL13337/co-37211-1/v%{version}_mibs.zip
# Source0-md5:	9f85e4a28b988289ec26580c0fadade1
URL:		http://www.hp.com/rnd/software/MIBs.htm
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIBs for B-Series HP StorageWorks SAN Switches that run v5.x firmware.

%description -l pl.UTF-8
MIB-y dla switchy HP StorageWorks serii B z firmware w wersji 5.x.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

for file in *.mib; do
	b=$(basename "$file" .mib)
	install "$file" $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/mib-${b}.txt
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf
%{_datadir}/snmp/mibs/*.*
