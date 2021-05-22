#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Base
Version  : 0.09
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Base-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Base-0.09.tar.gz
Summary  : 'useful base class for deriving other modules '
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Base-license = %{version}-%{release}
Requires: perl-Class-Base-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)

%description
NAME
Class::Base - useful base class for deriving other modules
SYNOPSIS
package My::Funky::Module;
use base qw( Class::Base );

%package dev
Summary: dev components for the perl-Class-Base package.
Group: Development
Provides: perl-Class-Base-devel = %{version}-%{release}
Requires: perl-Class-Base = %{version}-%{release}

%description dev
dev components for the perl-Class-Base package.


%package license
Summary: license components for the perl-Class-Base package.
Group: Default

%description license
license components for the perl-Class-Base package.


%package perl
Summary: perl components for the perl-Class-Base package.
Group: Default
Requires: perl-Class-Base = %{version}-%{release}

%description perl
perl components for the perl-Class-Base package.


%prep
%setup -q -n Class-Base-0.09
cd %{_builddir}/Class-Base-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Base
cp %{_builddir}/Class-Base-0.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Base/9102d582aed83299d9d5526f94af9fbacd0ca776
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Base.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Base/9102d582aed83299d9d5526f94af9fbacd0ca776

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Class/Base.pm
