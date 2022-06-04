#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-strictures
Version  : 2.000006
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/strictures-2.000006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/strictures-2.000006.tar.gz
Summary  : 'Turn on strict and make most warnings fatal'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-strictures-license = %{version}-%{release}
Requires: perl-strictures-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(bareword::filehandles)
BuildRequires : perl(indirect)
BuildRequires : perl(multidimensional)

%description
NAME
strictures - Turn on strict and make most warnings fatal
SYNOPSIS
use strictures 2;

%package dev
Summary: dev components for the perl-strictures package.
Group: Development
Provides: perl-strictures-devel = %{version}-%{release}
Requires: perl-strictures = %{version}-%{release}

%description dev
dev components for the perl-strictures package.


%package license
Summary: license components for the perl-strictures package.
Group: Default

%description license
license components for the perl-strictures package.


%package perl
Summary: perl components for the perl-strictures package.
Group: Default
Requires: perl-strictures = %{version}-%{release}

%description perl
perl components for the perl-strictures package.


%prep
%setup -q -n strictures-2.000006
cd %{_builddir}/strictures-2.000006

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-strictures
cp %{_builddir}/strictures-2.000006/LICENSE %{buildroot}/usr/share/package-licenses/perl-strictures/9ef6cb6bf8daa686a87a0d40ac8adcc38ff0a71c
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
/usr/share/man/man3/strictures.3
/usr/share/man/man3/strictures::extra.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-strictures/9ef6cb6bf8daa686a87a0d40ac8adcc38ff0a71c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
