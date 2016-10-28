.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_cs.c

.. _`radeon_cs_parser_fini`:

radeon_cs_parser_fini
=====================

.. c:function:: void radeon_cs_parser_fini(struct radeon_cs_parser *parser, int error, bool backoff)

    clean parser states

    :param struct radeon_cs_parser \*parser:
        parser structure holding parsing context.

    :param int error:
        error number

    :param bool backoff:
        *undescribed*

.. _`radeon_cs_parser_fini.description`:

Description
-----------

If error is set than unvalidate buffer, otherwise just free memory
used by parsing context.

.. _`radeon_cs_packet_parse`:

radeon_cs_packet_parse
======================

.. c:function:: int radeon_cs_packet_parse(struct radeon_cs_parser *p, struct radeon_cs_packet *pkt, unsigned idx)

    parse cp packet and point ib index to next packet

    :param struct radeon_cs_parser \*p:
        *undescribed*

    :param struct radeon_cs_packet \*pkt:
        where to store packet information

    :param unsigned idx:
        *undescribed*

.. _`radeon_cs_packet_parse.description`:

Description
-----------

Assume that chunk_ib_index is properly set. Will return -EINVAL
if packet is bigger than remaining ib size. or if packets is unknown.

.. _`radeon_cs_packet_next_is_pkt3_nop`:

radeon_cs_packet_next_is_pkt3_nop
=================================

.. c:function:: bool radeon_cs_packet_next_is_pkt3_nop(struct radeon_cs_parser *p)

    test if the next packet is P3 NOP

    :param struct radeon_cs_parser \*p:
        structure holding the parser context.

.. _`radeon_cs_packet_next_is_pkt3_nop.description`:

Description
-----------

Check if the next packet is NOP relocation packet3.

.. _`radeon_cs_dump_packet`:

radeon_cs_dump_packet
=====================

.. c:function:: void radeon_cs_dump_packet(struct radeon_cs_parser *p, struct radeon_cs_packet *pkt)

    dump raw packet context

    :param struct radeon_cs_parser \*p:
        structure holding the parser context.

    :param struct radeon_cs_packet \*pkt:
        structure holding the packet.

.. _`radeon_cs_dump_packet.description`:

Description
-----------

Used mostly for debugging and error reporting.

.. _`radeon_cs_packet_next_reloc`:

radeon_cs_packet_next_reloc
===========================

.. c:function:: int radeon_cs_packet_next_reloc(struct radeon_cs_parser *p, struct radeon_bo_list **cs_reloc, int nomm)

    parse next (should be reloc) packet

    :param struct radeon_cs_parser \*p:
        *undescribed*

    :param struct radeon_bo_list \*\*cs_reloc:
        *undescribed*

    :param int nomm:
        *undescribed*

.. _`radeon_cs_packet_next_reloc.description`:

Description
-----------

Check if next packet is relocation packet3, do bo validation and compute
GPU offset using the provided start.

.. This file was automatic generated / don't edit.

