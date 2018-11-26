.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3pf/hclge_cmd.c

.. _`hclge_cmd_send`:

hclge_cmd_send
==============

.. c:function:: int hclge_cmd_send(struct hclge_hw *hw, struct hclge_desc *desc, int num)

    send command to command queue

    :param hw:
        pointer to the hw struct
    :type hw: struct hclge_hw \*

    :param desc:
        prefilled descriptor for describing the command
    :type desc: struct hclge_desc \*

    :param num:
        the number of descriptors to be sent
    :type num: int

.. _`hclge_cmd_send.description`:

Description
-----------

This is the main send command for command queue, it
sends the queue, cleans the queue, etc

.. This file was automatic generated / don't edit.

