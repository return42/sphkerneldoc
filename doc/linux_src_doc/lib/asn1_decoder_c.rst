.. -*- coding: utf-8; mode: rst -*-

==============
asn1_decoder.c
==============


.. _`asn1_ber_decoder`:

asn1_ber_decoder
================

.. c:function:: int asn1_ber_decoder (const struct asn1_decoder *decoder, void *context, const unsigned char *data, size_t datalen)

    Decoder BER/DER/CER ASN.1 according to pattern

    :param const struct asn1_decoder \*decoder:
        The decoder definition (produced by asn1_compiler)

    :param void \*context:
        The caller's context (to be passed to the action functions)

    :param const unsigned char \*data:
        The encoded data

    :param size_t datalen:
        The size of the encoded data



.. _`asn1_ber_decoder.description`:

Description
-----------

Decode BER/DER/CER encoded ASN.1 data according to a bytecode pattern
produced by asn1_compiler.  Action functions are called on marked tags to
allow the caller to retrieve significant data.



.. _`asn1_ber_decoder.limitations`:

LIMITATIONS
-----------


To keep down the amount of stack used by this function, the following limits



.. _`asn1_ber_decoder.have-been-imposed`:

have been imposed
-----------------


(1) This won't handle datalen > 65535 without increasing the size of the
cons stack elements and length_too_long checking.

(2) The stack of constructed types is 10 deep.  If the depth of non-leaf
constructed types exceeds this, the decode will fail.

(3) The SET type (not the SET OF type) isn't really supported as tracking
what members of the set have been seen is a pain.

