.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/crc32.h

.. _`crc32_posix_end`:

crc32_posix_end
===============

.. c:function:: u32 crc32_posix_end(u32 crc, size_t total_len)

    Finalize POSIX CRC32 working state

    :param crc:
        Current CRC32 working state
    :type crc: u32

    :param total_len:
        Total length of data that was CRC32'd
    :type total_len: size_t

.. _`crc32_posix_end.return`:

Return
------

Final POSIX CRC32 value

.. This file was automatic generated / don't edit.

