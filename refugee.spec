Summary:	File encryption utility
Summary(pl):	Narzêdzie do szyfrowania plików
Name:		refugee
Version:	0.99
Release:	1
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.synack.com/src/%{name}-%{version}.tar.gz
BuildRequires:	libpng-devel
URL:		http://www.synack.com/soft.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Refugee is a file encryption and steganography utility. It implements
Blowfish and Rijndael in CBC mode and is portable between big- and
little-endian platforms. It supports key sizes from 32-448 bits and
gives the user many ways to make keys. It currently supports hiding
user data in PNG files.

%description -l pl
Refugee to narzêdzie do szyfrowania plików i steganografii.
Implementuje algorytmy Blowfish i Rijndael w trybie CBC i jest
przeno¶ny miêdzy platformami typu big- i little-endian. Mo¿e korzystaæ
z kluczy od 32 do 448 bitów, daj±c przy tym u¿ytkownikowi wiele
róznych sposobów na stworzenie klucza. W chwili obecnej refugee
umo¿liwia ukrywanie danych u¿ytkownika w plikach PNG.

%prep
%setup  -q

%build
./setup.sh
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -IRijndael \
	-funroll-loops -fomit-frame-pointer \
	-fno-strength-reduce -ffast-math" \
	PNG_LIB="-lpng"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

gzip -9nf BUGS CHANGES CRYPTO README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
