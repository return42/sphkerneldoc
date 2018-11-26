.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wireless/radiotap.c

.. _`ieee80211_radiotap_iterator_init`:

ieee80211_radiotap_iterator_init
================================

.. c:function:: int ieee80211_radiotap_iterator_init(struct ieee80211_radiotap_iterator *iterator, struct ieee80211_radiotap_header *radiotap_header, int max_length, const struct ieee80211_radiotap_vendor_namespaces *vns)

    radiotap parser iterator initialization

    :param iterator:
        radiotap_iterator to initialize
    :type iterator: struct ieee80211_radiotap_iterator \*

    :param radiotap_header:
        radiotap header to parse
    :type radiotap_header: struct ieee80211_radiotap_header \*

    :param max_length:
        total length we can parse into (eg, whole packet length)
    :type max_length: int

    :param vns:
        *undescribed*
    :type vns: const struct ieee80211_radiotap_vendor_namespaces \*

.. _`ieee80211_radiotap_iterator_init.return`:

Return
------

0 or a negative error code if there is a problem.

This function initializes an opaque iterator struct which can then
be passed to \ :c:func:`ieee80211_radiotap_iterator_next`\  to visit every radiotap
argument which is present in the header.  It knows about extended
present headers and handles them.

.. _`ieee80211_radiotap_iterator_init.how-to-use`:

How to use
----------

call \__ieee80211_radiotap_iterator_init() to init a semi-opaque iterator
struct ieee80211_radiotap_iterator (no need to init the struct beforehand)
checking for a good 0 return code.  Then loop calling
\__ieee80211_radiotap_iterator_next()... it returns either 0,
-ENOENT if there are no more args to parse, or -EINVAL if there is a problem.
The iterator's \ ``this_arg``\  member points to the start of the argument
associated with the current argument index that is present, which can be
found in the iterator's \ ``this_arg_index``\  member.  This arg index corresponds
to the IEEE80211_RADIOTAP_... defines.

.. _`ieee80211_radiotap_iterator_init.radiotap-header-length`:

Radiotap header length
----------------------

You can find the CPU-endian total radiotap header length in
iterator->max_length after executing \ :c:func:`ieee80211_radiotap_iterator_init`\ 
successfully.

.. _`ieee80211_radiotap_iterator_init.alignment-gotcha`:

Alignment Gotcha
----------------

You must take care when dereferencing iterator.this_arg
for multibyte types... the pointer is not aligned.  Use
get_unaligned((type \*)iterator.this_arg) to dereference
iterator.this_arg for type "type" safely on all arches.

.. _`ieee80211_radiotap_iterator_init.example-code`:

Example code
------------

See Documentation/networking/radiotap-headers.txt

.. _`ieee80211_radiotap_iterator_next`:

ieee80211_radiotap_iterator_next
================================

.. c:function:: int ieee80211_radiotap_iterator_next(struct ieee80211_radiotap_iterator *iterator)

    return next radiotap parser iterator arg

    :param iterator:
        radiotap_iterator to move to next arg (if any)
    :type iterator: struct ieee80211_radiotap_iterator \*

.. _`ieee80211_radiotap_iterator_next.return`:

Return
------

0 if there is an argument to handle,
-ENOENT if there are no more args or -EINVAL
if there is something else wrong.

This function provides the next radiotap arg index (IEEE80211_RADIOTAP\_\*)
in \ ``this_arg_index``\  and sets \ ``this_arg``\  to point to the
payload for the field.  It takes care of alignment handling and extended
present fields.  \ ``this_arg``\  can be changed by the caller (eg,
incremented to move inside a compound argument like
IEEE80211_RADIOTAP_CHANNEL).  The args pointed to are in
little-endian format whatever the endianess of your CPU.

.. _`ieee80211_radiotap_iterator_next.alignment-gotcha`:

Alignment Gotcha
----------------

You must take care when dereferencing iterator.this_arg
for multibyte types... the pointer is not aligned.  Use
get_unaligned((type \*)iterator.this_arg) to dereference
iterator.this_arg for type "type" safely on all arches.

.. This file was automatic generated / don't edit.

