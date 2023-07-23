%define upstream_name    Test-ConsistentVersion

Name:       perl-%{upstream_name}
Version:    0.3.1
Release:    1

Summary:    Ensures distribution versions are consistent
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-v%{version}.tar.gz

BuildRequires: perl(Test::Builder)
BuildRequires: perl(autodie)
BuildRequires: perl(version)
BuildRequires: perl(Module::Build)
BuildArch: noarch

%description
The purpose of this module is to make it easy for other distribution
authors to have consistent version numbers within the modules (as well as
readme file and changelog) of the distribution.

%prep
%autosetup -p1 -n %{upstream_name}-v%{version}
perl Build.PL installdirs=vendor destdir="%{buildroot}"

%build
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
