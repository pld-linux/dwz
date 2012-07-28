Summary:	DWARF optimization and duplicate removal tool
Name:		dwz
Version:	0.6
Release:	1
License:	GPL v2+ and GPL v3+
Group:		Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=%{name}-%{version}/ %{name}-%{version} \
#   | bzip2 -9 > %{name}-%{version}.tar.bz2
# using fedora tarballs from http://pkgs.fedoraproject.org/repo/pkgs/dwz/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e72adeacdae79647f34f139f7957bcb1
BuildRequires:	elfutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF
executables for size, by replacing DWARF information representation
with equivalent smaller representation where possible and by reducing
the amount of duplication using techniques from DWARF standard
appendix E - creating DW_TAG_partial_unit compilation units (CUs) for
duplicated information and using DW_TAG_imported_unit to import it
into each CU that needs it.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	bindir=%{_bindir} \
	%{nil}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	bindir=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.RUNTIME
%attr(755,root,root) %{_bindir}/dwz
%{_mandir}/man1/dwz.1*
