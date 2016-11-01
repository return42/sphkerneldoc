.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kernel/dis.c

.. _`insn_to_mnemonic`:

insn_to_mnemonic
================

.. c:function:: int insn_to_mnemonic(unsigned char *instruction, char *buf, unsigned int len)

    decode an s390 instruction

    :param unsigned char \*instruction:
        instruction to decode

    :param char \*buf:
        buffer to fill with mnemonic

    :param unsigned int len:
        length of buffer

.. _`insn_to_mnemonic.description`:

Description
-----------

Decode the instruction at \ ``instruction``\  and store the corresponding
mnemonic into \ ``buf``\  of length \ ``len``\ .
\ ``buf``\  is left unchanged if the instruction could not be decoded.

.. _`insn_to_mnemonic.return`:

Return
------

%0 on success, \ ``-ENOENT``\  if the instruction was not found.

.. This file was automatic generated / don't edit.

