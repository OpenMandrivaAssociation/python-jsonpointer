%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:	2.4
Release:	1
Summary:        Library to resolve JSON pointers according to RFC 6901
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonpointer
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
Library to resolve JSON pointers according to RFC 6901

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{_bindir}/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
