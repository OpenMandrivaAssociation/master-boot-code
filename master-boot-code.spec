Name:		master-boot-code
License:	BSD 3-Clause
Group:		System/Kernel and hardware
Version:	1.14
Release:	2
Summary:	i386 Master Boot Record Code
URL:		http://www.novell.com/products/linuxpackages/opensuse/master-boot-code.html
Source0:	master-boot-code.tar.bz2
Source1:	%{name}.rpmlintrc
Exclusivearch:	%ix86 x86_64 amd64 ia32e

Patch0:		master-boot-code-x86_64.patch

%description
The i386 master boot code is code that, after copied to the MBR of the
boot disk, loads and starts the boot sector of the active partition.

Authors:
--------
    Wolfgang Solfrank, TooLs GmbH
    The Regents of the University of California

%prep
%setup -n %{name}-%{version}

%ifarch x86_64
%patch0 -p1
%endif

%build
make

%install
test -d %{buildroot}/usr/lib/boot || mkdir -p %{buildroot}/usr/lib/boot
install -c -p -m 644 mbr %{buildroot}/usr/lib/boot/master-boot-code

%files
%dir /usr/lib/boot
%attr(644,root,root) /usr/lib/boot/master-boot-code
%doc COPYING


%changelog
* Wed Jun 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.14-1
+ Revision: 683121
- Import OpenSUSE master-boot-code package, version 1.14
- Import master-boot-code

