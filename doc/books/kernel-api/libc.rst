
.. _libc:

=========================
Basic C Library Functions
=========================

When writing drivers, you cannot in general use routines which are from the C Library. Some of the functions have been found generally useful and they are listed below. The
behaviour of these functions may vary slightly from those defined by ANSI, and these deviations are noted in the text.


String Conversions
==================


.. toctree::
    :maxdepth: 1

    API-simple-strtoull
    API-simple-strtoul
    API-simple-strtol
    API-simple-strtoll
    API-vsnprintf
    API-vscnprintf
    API-snprintf
    API-scnprintf
    API-vsprintf
    API-sprintf
    API-vbin-printf
    API-bstr-printf
    API-bprintf
    API-vsscanf
    API-sscanf
    API-kstrtol
    API-kstrtoul
    API-kstrtoull
    API-kstrtoll
    API-kstrtouint
    API-kstrtoint
    API-kstrtobool

String Manipulation
===================


.. toctree::
    :maxdepth: 1

    API-strncasecmp
    API-strcpy
    API-strncpy
    API-strlcpy
    API-strscpy
    API-strcat
    API-strncat
    API-strlcat
    API-strcmp
    API-strncmp
    API-strchr
    API-strchrnul
    API-strrchr
    API-strnchr
    API-skip-spaces
    API-strim
    API-strlen
    API-strnlen
    API-strspn
    API-strcspn
    API-strpbrk
    API-strsep
    API-sysfs-streq
    API-match-string
    API-memset
    API-memzero-explicit
    API-memcpy
    API-memmove
    API-memcmp
    API-memscan
    API-strstr
    API-strnstr
    API-memchr
    API-memchr-inv
    API-strreplace

Bit Operations
==============


.. toctree::
    :maxdepth: 1

    API-set-bit
    API---set-bit
    API-clear-bit
    API---change-bit
    API-change-bit
    API-test-and-set-bit
    API-test-and-set-bit-lock
    API---test-and-set-bit
    API-test-and-clear-bit
    API---test-and-clear-bit
    API-test-and-change-bit
    API-test-bit
    API---ffs
    API-ffz
    API-ffs
    API-fls
    API-fls64
