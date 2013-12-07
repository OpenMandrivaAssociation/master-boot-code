Summary:	i386 Master Boot Record Code
Name:		master-boot-code
License:	BSD 3-Clause
Group:		System/Kernel and hardware
Version:	1.14
Release:	4
Url:		http://www.novell.com/products/linuxpackages/opensuse/master-boot-code.html
Source0:	master-boot-code.tar.bz2
Source1:	%{name}.rpmlintrc
Patch0:		master-boot-code-x86_64.patch
Exclusivearch:	%ix86 x86_64 amd64 ia32e

%description
The i386 master boot code is code that, after copied to the MBR of the
boot disk, loads and starts the boot sector of the active partition.

Authors:
--------
    Wolfgang Solfrank, TooLs GmbH
    The Regents of the University of California

%prep
%setup -q

%ifarch x86_64
%patch0 -p1
%endif

%build
make

%install
test -d %{buildroot}/usr/lib/boot || mkdir -p %{buildroot}/usr/lib/boot
install -c -p -m 644 mbr %{buildroot}/usr/lib/boot/master-boot-code

%files
%doc COPYING
%dir /usr/lib/boot
%attr(644,root,root) /usr/lib/boot/master-boot-code

