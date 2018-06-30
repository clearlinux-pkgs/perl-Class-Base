#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Base
Version  : 0.09
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Base-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Base-0.09.tar.gz
Summary  : 'useful base class for deriving other modules '
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-Base-man
BuildRequires : perl(Clone)

%description
NAME
Class::Base - useful base class for deriving other modules
SYNOPSIS
package My::Funky::Module;
use base qw( Class::Base );

%package man
Summary: man components for the perl-Class-Base package.
Group: Default

%description man
man components for the perl-Class-Base package.


%prep
%setup -q -n Class-Base-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Class/Base.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Base.3
