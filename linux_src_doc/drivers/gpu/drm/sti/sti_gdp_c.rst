.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_gdp.c

.. _`sti_gdp_get_free_nodes`:

sti_gdp_get_free_nodes
======================

.. c:function:: struct sti_gdp_node_list *sti_gdp_get_free_nodes(struct sti_gdp *gdp)

    :param gdp:
        gdp pointer
    :type gdp: struct sti_gdp \*

.. _`sti_gdp_get_free_nodes.description`:

Description
-----------

Look for a GDP node list that is not currently read by the HW.

.. _`sti_gdp_get_free_nodes.return`:

Return
------

Pointer to the free GDP node list

.. _`sti_gdp_get_current_nodes`:

sti_gdp_get_current_nodes
=========================

.. c:function:: struct sti_gdp_node_list *sti_gdp_get_current_nodes(struct sti_gdp *gdp)

    :param gdp:
        gdp pointer
    :type gdp: struct sti_gdp \*

.. _`sti_gdp_get_current_nodes.description`:

Description
-----------

Look for GDP nodes that are currently read by the HW.

.. _`sti_gdp_get_current_nodes.return`:

Return
------

Pointer to the current GDP node list

.. _`sti_gdp_disable`:

sti_gdp_disable
===============

.. c:function:: void sti_gdp_disable(struct sti_gdp *gdp)

    :param gdp:
        gdp pointer
    :type gdp: struct sti_gdp \*

.. _`sti_gdp_disable.description`:

Description
-----------

Disable a GDP.

.. _`sti_gdp_field_cb`:

sti_gdp_field_cb
================

.. c:function:: int sti_gdp_field_cb(struct notifier_block *nb, unsigned long event, void *data)

    :param nb:
        notifier block
    :type nb: struct notifier_block \*

    :param event:
        event message
    :type event: unsigned long

    :param data:
        private data
    :type data: void \*

.. _`sti_gdp_field_cb.description`:

Description
-----------

Handle VTG top field and bottom field event.

.. _`sti_gdp_field_cb.return`:

Return
------

0 on success.

.. _`sti_gdp_get_dst`:

sti_gdp_get_dst
===============

.. c:function:: int sti_gdp_get_dst(struct device *dev, int dst, int src)

    :param dev:
        device
    :type dev: struct device \*

    :param dst:
        requested destination size
    :type dst: int

    :param src:
        source size
    :type src: int

.. _`sti_gdp_get_dst.description`:

Description
-----------

Return the cropped / clamped destination size

.. _`sti_gdp_get_dst.return`:

Return
------

cropped / clamped destination size

.. This file was automatic generated / don't edit.

