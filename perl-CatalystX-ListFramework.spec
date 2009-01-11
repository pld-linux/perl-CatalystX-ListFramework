#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CatalystX
%define	pnam	ListFramework
Summary:	CatalystX::ListFramework - foundations for displaying and editing lists (CRUD) in a Catalyst application
#Summary(pl.UTF-8):	
Name:		perl-CatalystX-ListFramework
Version:	0.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CatalystX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e9a93c059a250e8c4865c59cd8a63693
URL:		http://search.cpan.org/dist/CatalystX-ListFramework/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst::View::JSON)
BuildRequires:	perl(DBD::SQLite2)
BuildRequires:	perl(HTML::Widget)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Catalyst-Plugin-HTML-Widget
BuildRequires:	perl-Catalyst-Plugin-StackTrace
BuildRequires:	perl-Test-use-ok
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displaying tabulated lists of database records, updating those records and
creating new ones is a common task in Catalyst applications.
This class supplies such lists, and forms to edit such records, to a set of
templates, using simple definition files and your DBIx::Class Catalyst
model. A search form is also supplied, which can include JSON-powered
ExtJS comboboxes (see http://www.extjs.com/).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/CatalystX/*.pm
%{perl_vendorlib}/CatalystX/ListFramework
%{_mandir}/man3/*
