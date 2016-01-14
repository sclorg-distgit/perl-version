%{?scl:%scl_package perl-version}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-version
Epoch:          3
Version:        0.99.07
%global module_version 0.9907
Release:        1%{?dist}
Summary:        Perl extension for Version Objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/version/
Source0:        http://www.cpan.org/authors/id/J/JP/JPEACOCK/version-%{module_version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.13
BuildRequires:  %{?scl_prefix}perl(if)
# IO::Handle is optional
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(locale)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.45
BuildRequires:  %{?scl_prefix}perl(Test::Harness)
BuildRequires:  %{?scl_prefix}perl(UNIVERSAL)
BuildRequires:  %{?scl_prefix}perl(vars)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(locale)
Requires:       %{?scl_prefix}perl(UNIVERSAL)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}
# version::vxs is private module (see bug #633775)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(version::vxs\\)

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_provides /perl(version::vxs)/d
%filter_setup
%endif

%description
Version objects were added to Perl in 5.10. This module implements version
objects for older version of Perl and provides the version object API for
all versions of Perl. All previous releases before 0.74 are deprecated and
should not be used due to incompatible API changes. Version 0.77 introduces
the new 'parse' and 'declare' methods to standardize usage. You are
strongly urged to set 0.77 as a minimum in your code.

%prep
%setup -q -n version-%{module_version}

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%doc %{perl_vendorarch}/version.pod
%dir %{perl_vendorarch}/version/
%doc %{perl_vendorarch}/version/Internals.pod
%{perl_vendorarch}/auto/version/
%{perl_vendorarch}/version.pm
%{perl_vendorarch}/version/vpp.pm
%{perl_vendorarch}/version/vxs.pm
%{perl_vendorarch}/version/regex.pm
%{_mandir}/man3/version.3pm*
%{_mandir}/man3/version::Internals.3pm*

%changelog
* Wed Jan 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3:0.99.07-1
- 0.9907 bump
- Resolves: rhbz#1059183

* Wed Nov 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3:0.99.04-1
- 0.9904 bump

* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3:0.99.02-1
- 0.9902 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3:0.99.01-1
- SCL package - initial import
