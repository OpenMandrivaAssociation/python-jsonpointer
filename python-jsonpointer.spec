%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:	3.0.0
Release:	2
Summary:        Library to resolve JSON pointers according to RFC 6901
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonpointer
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)

%description
Library to resolve JSON pointers according to RFC 6901

%files
%{_bindir}/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
