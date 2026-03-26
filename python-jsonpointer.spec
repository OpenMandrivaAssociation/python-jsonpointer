%define module jsonpointer

Name:		python-jsonpointer
Version:	3.1.1
Release:	1
Summary:	Library to resolve JSON pointers according to RFC 6901
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/jsonpointer
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
Library to resolve JSON pointers according to RFC 6901.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{_bindir}/%{module}
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}*.*-info
