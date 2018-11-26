.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/desc_constr.h

.. _`alginfo`:

struct alginfo
==============

.. c:type:: struct alginfo

    Container for algorithm details

.. _`alginfo.definition`:

Definition
----------

.. code-block:: c

    struct alginfo {
        u32 algtype;
        unsigned int keylen;
        unsigned int keylen_pad;
        union {
            dma_addr_t key_dma;
            const void *key_virt;
        } ;
        bool key_inline;
    }

.. _`alginfo.members`:

Members
-------

algtype
    algorithm selector; for valid values, see documentation of the
    functions where it is used.

keylen
    length of the provided algorithm key, in bytes

keylen_pad
    padded length of the provided algorithm key, in bytes

{unnamed_union}
    anonymous

key_dma
    *undescribed*

key_virt
    *undescribed*

key_inline
    true - key can be inlined in the descriptor; false - key is
    referenced by the descriptor

.. _`desc_inline_query`:

desc_inline_query
=================

.. c:function:: int desc_inline_query(unsigned int sd_base_len, unsigned int jd_len, unsigned int *data_len, u32 *inl_mask, unsigned int count)

    Provide indications on which data items can be inlined and which shall be referenced in a shared descriptor.

    :param sd_base_len:
        Shared descriptor base length - bytes consumed by the commands,
        excluding the data items to be inlined (or corresponding
        pointer if an item is not inlined). Each cnstr\_\* function that
        generates descriptors should have a define mentioning
        corresponding length.
    :type sd_base_len: unsigned int

    :param jd_len:
        Maximum length of the job descriptor(s) that will be used
        together with the shared descriptor.
    :type jd_len: unsigned int

    :param data_len:
        Array of lengths of the data items trying to be inlined
    :type data_len: unsigned int \*

    :param inl_mask:
        32bit mask with bit x = 1 if data item x can be inlined, 0
        otherwise.
    :type inl_mask: u32 \*

    :param count:
        Number of data items (size of \ ``data_len``\  array); must be <= 32
    :type count: unsigned int

.. _`desc_inline_query.return`:

Return
------

0 if data can be inlined / referenced, negative value if not. If 0,
check \ ``inl_mask``\  for details.

.. _`append_proto_dkp`:

append_proto_dkp
================

.. c:function:: void append_proto_dkp(u32 * const desc, struct alginfo *adata)

    Derived Key Protocol (DKP): key -> split key

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param adata:
        pointer to authentication transform definitions.
        keylen should be the length of initial key, while keylen_pad
        the length of the derived (split) key.
        Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1, SHA224,
        SHA256, SHA384, SHA512}.
    :type adata: struct alginfo \*

.. This file was automatic generated / don't edit.

