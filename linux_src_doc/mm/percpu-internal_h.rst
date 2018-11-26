.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/percpu-internal.h

.. _`pcpu_chunk_nr_blocks`:

pcpu_chunk_nr_blocks
====================

.. c:function:: int pcpu_chunk_nr_blocks(struct pcpu_chunk *chunk)

    converts nr_pages to # of md_blocks

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

.. _`pcpu_chunk_nr_blocks.description`:

Description
-----------

This conversion is from the number of physical pages that the chunk
serves to the number of bitmap blocks used.

.. _`pcpu_nr_pages_to_map_bits`:

pcpu_nr_pages_to_map_bits
=========================

.. c:function:: int pcpu_nr_pages_to_map_bits(int pages)

    converts the pages to size of bitmap

    :param pages:
        number of physical pages
    :type pages: int

.. _`pcpu_nr_pages_to_map_bits.description`:

Description
-----------

This conversion is from physical pages to the number of bits
required in the bitmap.

.. _`pcpu_chunk_map_bits`:

pcpu_chunk_map_bits
===================

.. c:function:: int pcpu_chunk_map_bits(struct pcpu_chunk *chunk)

    helper to convert nr_pages to size of bitmap

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

.. _`pcpu_chunk_map_bits.description`:

Description
-----------

This conversion is from the number of physical pages that the chunk
serves to the number of bits in the bitmap.

.. This file was automatic generated / don't edit.

