Summary:	File encryption utility
Summary(pl):	Narz�dzie do szyfrowania plik�w
Name:		refugee
Version:	0.99
Release:	3
License:	GPL
Group:		Applications/File
Source0:	http://www.synack.com/src/%{name}-%{version}.tar.gz
URL:		http://www.synack.com/soft.html
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Refugee is a file encryption and steganography utility. It implements
Blowfish and Rijndael in CBC mode and is portable between big- and
little-endian platforms. It supports key sizes from 32-448 bits and
gives the user many ways to make keys. It currently supports hiding
user data in PNG files.

%description -l pl
Refugee to narz�dzie do szyfrowania plik�w i steganografii.
Implementuje algorytmy Blowfish i Rijndael w trybie CBC i jest
przeno�ny mi�dzy platformami typu big- i little-endian. Mo�e korzysta�
z kluczy od 32 do 448 bit�w, daj�c przy tym u�ytkownikowi wiele
r�znych sposob�w na stworzenie klucza. W chwili obecnej refugee
umo�liwia ukrywanie danych u�ytkownika w plikach PNG.

%prep
%setup  -q

%build
./setup.sh
%{__make} CFLAGS="%{rpmcflags} -IRijndael \
	%{!?debug:-funroll-loops -fomit-frame-pointer} \
	-fno-strength-reduce -ffast-math" \
	PNG_LIB="-lpng"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

# names are too common...
cd $RPM_BUILD_ROOT%{_bindir}
for f in decrypt encrypt hide key ; do
	mv -f $f refugee-$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CRYPTO README TODO
%attr(755,root,root) %{_bindir}/*
