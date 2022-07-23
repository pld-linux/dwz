Summary:	DWARF optimization and duplicate removal tool
Summary(pl.UTF-8):	Narzędzie do optymalizacji DWARF i usuwania duplikatów
Name:		dwz
Version:	0.14
Release:	1
License:	GPL v2+ and GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Tools
Source0:	ftp://sourceware.org/pub/dwz/releases/%{name}-%{version}.tar.xz
# Source0-md5:	1f1225898bd40d63041d54454fcda5b6
URL:		http://www.sourceware.org/dwz/
BuildRequires:	elfutils-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%description -l pl.UTF-8
Pakiet dwz zawiera program próbujący zoptymalizować informacje DWARF
dla debuggerów, zawarte w bibliotekach współdzielonych i plikach
wykonywalnych ELF, pod kątem rozmiaru, zastępując reprezentację
informacji DWARF równoważną o mniejszym rozmiarze oraz zmniejszając
stopień duplikacji przy użyciu technik opisanych w załączniku E do
standardu DWARF - poprzez tworzenie jednostek kompilacji (CU)
DW_TAG_partial_unit dla informacji zduplikowanych oraz używanie
DW_TAG_imported_unit do importowania ich w każdej CU, która ich
wymaga.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.RUNTIME
%attr(755,root,root) %{_bindir}/dwz
%{_mandir}/man1/dwz.1*
