.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_mbox.c

.. _`lpfc_dump_static_vport`:

lpfc_dump_static_vport
======================

.. c:function:: int lpfc_dump_static_vport(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, uint16_t offset)

    Dump HBA's static vport information.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param uint16_t offset:
        offset for dumping vport info.

.. _`lpfc_dump_static_vport.description`:

Description
-----------

The dump mailbox command provides a method for the device driver to obtain
various types of information from the HBA device.

This routine prepares the mailbox command for dumping list of static
vports to be created.

.. _`lpfc_down_link`:

lpfc_down_link
==============

.. c:function:: void lpfc_down_link(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Bring down HBAs link.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_down_link.description`:

Description
-----------

This routine prepares a mailbox command to bring down HBA link.

.. _`lpfc_dump_mem`:

lpfc_dump_mem
=============

.. c:function:: void lpfc_dump_mem(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, uint16_t offset, uint16_t region_id)

    Prepare a mailbox command for reading a region.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param uint16_t offset:
        offset into the region.

    :param uint16_t region_id:
        config region id.

.. _`lpfc_dump_mem.description`:

Description
-----------

The dump mailbox command provides a method for the device driver to obtain
various types of information from the HBA device.

This routine prepares the mailbox command for dumping HBA's config region.

.. _`lpfc_dump_wakeup_param`:

lpfc_dump_wakeup_param
======================

.. c:function:: void lpfc_dump_wakeup_param(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare mailbox command for retrieving wakeup params

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_dump_wakeup_param.description`:

Description
-----------

This function create a dump memory mailbox command to dump wake up
parameters.

.. _`lpfc_read_nv`:

lpfc_read_nv
============

.. c:function:: void lpfc_read_nv(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for reading HBA's NVRAM param

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_read_nv.description`:

Description
-----------

The read NVRAM mailbox command returns the HBA's non-volatile parameters
that are used as defaults when the Fibre Channel link is brought on-line.

This routine prepares the mailbox command for reading information stored
in the HBA's NVRAM. Specifically, the HBA's WWNN and WWPN.

.. _`lpfc_config_async`:

lpfc_config_async
=================

.. c:function:: void lpfc_config_async(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, uint32_t ring)

    Prepare a mailbox command for enabling HBA async event

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param uint32_t ring:
        ring number for the asynchronous event to be configured.

.. _`lpfc_config_async.description`:

Description
-----------

The asynchronous event enable mailbox command is used to enable the
asynchronous event posting via the ASYNC_STATUS_CN IOCB response and
specifies the default ring to which events are posted.

This routine prepares the mailbox command for enabling HBA asynchronous
event support on a IOCB ring.

.. _`lpfc_heart_beat`:

lpfc_heart_beat
===============

.. c:function:: void lpfc_heart_beat(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for heart beat

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_heart_beat.description`:

Description
-----------

The heart beat mailbox command is used to detect an unresponsive HBA, which
is defined as any device where no error attention is sent and both mailbox
and rings are not processed.

This routine prepares the mailbox command for issuing a heart beat in the
form of mailbox command to the HBA. The timely completion of the heart
beat mailbox command indicates the health of the HBA.

.. _`lpfc_read_topology`:

lpfc_read_topology
==================

.. c:function:: int lpfc_read_topology(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, struct lpfc_dmabuf *mp)

    Prepare a mailbox command for reading HBA topology

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param struct lpfc_dmabuf \*mp:
        DMA buffer memory for reading the link attention information into.

.. _`lpfc_read_topology.description`:

Description
-----------

The read topology mailbox command is issued to read the link topology
information indicated by the HBA port when the Link Event bit of the Host
Attention (HSTATT) register is set to 1 (For SLI-3) or when an FC Link
Attention ACQE is received from the port (For SLI-4). A Link Event
Attention occurs based on an exception detected at the Fibre Channel link
interface.

This routine prepares the mailbox command for reading HBA link topology
information. A DMA memory has been set aside and address passed to the
HBA through \ ``mp``\  for the HBA to DMA link attention information into the
memory as part of the execution of the mailbox command.

Return codes
0 - Success (currently always return 0)

.. _`lpfc_clear_la`:

lpfc_clear_la
=============

.. c:function:: void lpfc_clear_la(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for clearing HBA link attention

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_clear_la.description`:

Description
-----------

The clear link attention mailbox command is issued to clear the link event
attention condition indicated by the Link Event bit of the Host Attention
(HSTATT) register. The link event attention condition is cleared only if
the event tag specified matches that of the current link event counter.
The current event tag is read using the read link attention event mailbox
command.

This routine prepares the mailbox command for clearing HBA link attention
information.

.. _`lpfc_config_link`:

lpfc_config_link
================

.. c:function:: void lpfc_config_link(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for configuring link on a HBA

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_config_link.description`:

Description
-----------

The configure link mailbox command is used before the initialize link
mailbox command to override default value and to configure link-oriented
parameters such as DID address and various timers. Typically, this
command would be used after an F_Port login to set the returned DID address
and the fabric timeout values. This command is not valid before a configure
port command has configured the HBA port.

This routine prepares the mailbox command for configuring link on a HBA.

.. _`lpfc_config_msi`:

lpfc_config_msi
===============

.. c:function:: int lpfc_config_msi(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for configuring msi-x

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_config_msi.description`:

Description
-----------

The configure MSI-X mailbox command is used to configure the HBA's SLI-3
MSI-X multi-message interrupt vector association to interrupt attention
conditions.

Return codes
0 - Success
-EINVAL - Failure

.. _`lpfc_init_link`:

lpfc_init_link
==============

.. c:function:: void lpfc_init_link(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, uint32_t topology, uint32_t linkspeed)

    Prepare a mailbox command for initialize link on a HBA

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param uint32_t topology:
        the link topology for the link to be initialized to.

    :param uint32_t linkspeed:
        the link speed for the link to be initialized to.

.. _`lpfc_init_link.description`:

Description
-----------

The initialize link mailbox command is used to initialize the Fibre
Channel link. This command must follow a configure port command that
establishes the mode of operation.

This routine prepares the mailbox command for initializing link on a HBA
with the specified link topology and speed.

.. _`lpfc_read_sparam`:

lpfc_read_sparam
================

.. c:function:: int lpfc_read_sparam(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb, int vpi)

    Prepare a mailbox command for reading HBA parameters

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param int vpi:
        virtual N_Port identifier.

.. _`lpfc_read_sparam.description`:

Description
-----------

The read service parameter mailbox command is used to read the HBA port
service parameters. The service parameters are read into the buffer
specified directly by a BDE in the mailbox command. These service
parameters may then be used to build the payload of an N_Port/F_POrt
login request and reply (LOGI/ACC).

This routine prepares the mailbox command for reading HBA port service
parameters. The DMA memory is allocated in this function and the addresses
are populated into the mailbox command for the HBA to DMA the service
parameters into.

Return codes
0 - Success
1 - DMA memory allocation failed

.. _`lpfc_unreg_did`:

lpfc_unreg_did
==============

.. c:function:: void lpfc_unreg_did(struct lpfc_hba *phba, uint16_t vpi, uint32_t did, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for unregistering DID

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t vpi:
        virtual N_Port identifier.

    :param uint32_t did:
        remote port identifier.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_unreg_did.description`:

Description
-----------

The unregister DID mailbox command is used to unregister an N_Port/F_Port
login for an unknown RPI by specifying the DID of a remote port. This
command frees an RPI context in the HBA port. This has the effect of
performing an implicit N_Port/F_Port logout.

This routine prepares the mailbox command for unregistering a remote
N_Port/F_Port (DID) login.

.. _`lpfc_read_config`:

lpfc_read_config
================

.. c:function:: void lpfc_read_config(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for reading HBA configuration

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_read_config.description`:

Description
-----------

The read configuration mailbox command is used to read the HBA port
configuration parameters. This mailbox command provides a method for
seeing any parameters that may have changed via various configuration
mailbox commands.

This routine prepares the mailbox command for reading out HBA configuration
parameters.

.. _`lpfc_read_lnk_stat`:

lpfc_read_lnk_stat
==================

.. c:function:: void lpfc_read_lnk_stat(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for reading HBA link stats

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_read_lnk_stat.description`:

Description
-----------

The read link status mailbox command is used to read the link status from
the HBA. Link status includes all link-related error counters. These
counters are maintained by the HBA and originated in the link hardware
unit. Note that all of these counters wrap.

This routine prepares the mailbox command for reading out HBA link status.

.. _`lpfc_reg_rpi`:

lpfc_reg_rpi
============

.. c:function:: int lpfc_reg_rpi(struct lpfc_hba *phba, uint16_t vpi, uint32_t did, uint8_t *param, LPFC_MBOXQ_t *pmb, uint16_t rpi)

    Prepare a mailbox command for registering remote login

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t vpi:
        virtual N_Port identifier.

    :param uint32_t did:
        remote port identifier.

    :param uint8_t \*param:
        pointer to memory holding the server parameters.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

    :param uint16_t rpi:
        the rpi to use in the registration (usually only used for SLI4.

.. _`lpfc_reg_rpi.description`:

Description
-----------

The registration login mailbox command is used to register an N_Port or
F_Port login. This registration allows the HBA to cache the remote N_Port
service parameters internally and thereby make the appropriate FC-2
decisions. The remote port service parameters are handed off by the driver
to the HBA using a descriptor entry that directly identifies a buffer in
host memory. In exchange, the HBA returns an RPI identifier.

This routine prepares the mailbox command for registering remote port login.
The function allocates DMA buffer for passing the service parameters to the
HBA with the mailbox command.

Return codes
0 - Success
1 - DMA memory allocation failed

.. _`lpfc_unreg_login`:

lpfc_unreg_login
================

.. c:function:: void lpfc_unreg_login(struct lpfc_hba *phba, uint16_t vpi, uint32_t rpi, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for unregistering remote login

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t vpi:
        virtual N_Port identifier.

    :param uint32_t rpi:
        remote port identifier

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_unreg_login.description`:

Description
-----------

The unregistration login mailbox command is used to unregister an N_Port
or F_Port login. This command frees an RPI context in the HBA. It has the
effect of performing an implicit N_Port/F_Port logout.

This routine prepares the mailbox command for unregistering remote port
login.

For SLI4 ports, the rpi passed to this function must be the physical
rpi value, not the logical index.

.. _`lpfc_sli4_unreg_all_rpis`:

lpfc_sli4_unreg_all_rpis
========================

.. c:function:: void lpfc_sli4_unreg_all_rpis(struct lpfc_vport *vport)

    unregister all RPIs for a vport on SLI4 HBA.

    :param struct lpfc_vport \*vport:
        pointer to a vport object.

.. _`lpfc_sli4_unreg_all_rpis.description`:

Description
-----------

This routine sends mailbox command to unregister all active RPIs for
a vport.

.. _`lpfc_reg_vpi`:

lpfc_reg_vpi
============

.. c:function:: void lpfc_reg_vpi(struct lpfc_vport *vport, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for registering vport identifier

    :param struct lpfc_vport \*vport:
        *undescribed*

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_reg_vpi.description`:

Description
-----------

The registration vport identifier mailbox command is used to activate a
virtual N_Port after it has acquired an N_Port_ID. The HBA validates the
N_Port_ID against the information in the selected virtual N_Port context
block and marks it active to allow normal processing of IOCB commands and
received unsolicited exchanges.

This routine prepares the mailbox command for registering a virtual N_Port.

.. _`lpfc_unreg_vpi`:

lpfc_unreg_vpi
==============

.. c:function:: void lpfc_unreg_vpi(struct lpfc_hba *phba, uint16_t vpi, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for unregistering vport id

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t vpi:
        virtual N_Port identifier.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_unreg_vpi.description`:

Description
-----------

The unregistration vport identifier mailbox command is used to inactivate
a virtual N_Port. The driver must have logged out and unregistered all
remote N_Ports to abort any activity on the virtual N_Port. The HBA will
unregisters any default RPIs associated with the specified vpi, aborting
any active exchanges. The HBA will post the mailbox response after making
the virtual N_Port inactive.

This routine prepares the mailbox command for unregistering a virtual
N_Port.

.. _`lpfc_config_pcb_setup`:

lpfc_config_pcb_setup
=====================

.. c:function:: void lpfc_config_pcb_setup(struct lpfc_hba *phba)

    Set up IOCB rings in the Port Control Block (PCB)

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_config_pcb_setup.description`:

Description
-----------

This routine sets up and initializes the IOCB rings in the Port Control
Block (PCB).

.. _`lpfc_read_rev`:

lpfc_read_rev
=============

.. c:function:: void lpfc_read_rev(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for reading HBA revision

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_read_rev.description`:

Description
-----------

The read revision mailbox command is used to read the revision levels of
the HBA components. These components include hardware units, resident
firmware, and available firmware. HBAs that supports SLI-3 mode of
operation provide different response information depending on the version
requested by the driver.

This routine prepares the mailbox command for reading HBA revision
information.

.. _`lpfc_build_hbq_profile2`:

lpfc_build_hbq_profile2
=======================

.. c:function:: void lpfc_build_hbq_profile2(struct config_hbq_var *hbqmb, struct lpfc_hbq_init *hbq_desc)

    Set up the HBQ Selection Profile 2

    :param struct config_hbq_var \*hbqmb:
        pointer to the HBQ configuration data structure in mailbox command.

    :param struct lpfc_hbq_init \*hbq_desc:
        pointer to the HBQ selection profile descriptor.

.. _`lpfc_build_hbq_profile2.description`:

Description
-----------

The Host Buffer Queue (HBQ) Selection Profile 2 specifies that the HBA
tests the incoming frames' R_CTL/TYPE fields with works 10:15 and performs
the Sequence Length Test using the fields in the Selection Profile 2
extension in words 20:31.

.. _`lpfc_build_hbq_profile3`:

lpfc_build_hbq_profile3
=======================

.. c:function:: void lpfc_build_hbq_profile3(struct config_hbq_var *hbqmb, struct lpfc_hbq_init *hbq_desc)

    Set up the HBQ Selection Profile 3

    :param struct config_hbq_var \*hbqmb:
        pointer to the HBQ configuration data structure in mailbox command.

    :param struct lpfc_hbq_init \*hbq_desc:
        pointer to the HBQ selection profile descriptor.

.. _`lpfc_build_hbq_profile3.description`:

Description
-----------

The Host Buffer Queue (HBQ) Selection Profile 3 specifies that the HBA
tests the incoming frame's R_CTL/TYPE fields with words 10:15 and performs
the Sequence Length Test and Byte Field Test using the fields in the
Selection Profile 3 extension in words 20:31.

.. _`lpfc_build_hbq_profile5`:

lpfc_build_hbq_profile5
=======================

.. c:function:: void lpfc_build_hbq_profile5(struct config_hbq_var *hbqmb, struct lpfc_hbq_init *hbq_desc)

    Set up the HBQ Selection Profile 5

    :param struct config_hbq_var \*hbqmb:
        pointer to the HBQ configuration data structure in mailbox command.

    :param struct lpfc_hbq_init \*hbq_desc:
        pointer to the HBQ selection profile descriptor.

.. _`lpfc_build_hbq_profile5.description`:

Description
-----------

The Host Buffer Queue (HBQ) Selection Profile 5 specifies a header HBQ. The
HBA tests the initial frame of an incoming sequence using the frame's
R_CTL/TYPE fields with words 10:15 and performs the Sequence Length Test
and Byte Field Test using the fields in the Selection Profile 5 extension
words 20:31.

.. _`lpfc_config_hbq`:

lpfc_config_hbq
===============

.. c:function:: void lpfc_config_hbq(struct lpfc_hba *phba, uint32_t id, struct lpfc_hbq_init *hbq_desc, uint32_t hbq_entry_index, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for configuring an HBQ

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint32_t id:
        HBQ identifier.

    :param struct lpfc_hbq_init \*hbq_desc:
        pointer to the HBA descriptor data structure.

    :param uint32_t hbq_entry_index:
        index of the HBQ entry data structures.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_config_hbq.description`:

Description
-----------

The configure HBQ (Host Buffer Queue) mailbox command is used to configure
an HBQ. The configuration binds events that require buffers to a particular
ring and HBQ based on a selection profile.

This routine prepares the mailbox command for configuring an HBQ.

.. _`lpfc_config_ring`:

lpfc_config_ring
================

.. c:function:: void lpfc_config_ring(struct lpfc_hba *phba, int ring, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for configuring an IOCB ring

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param int ring:
        *undescribed*

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_config_ring.description`:

Description
-----------

The configure ring mailbox command is used to configure an IOCB ring. This
configuration binds from one to six of HBA RC_CTL/TYPE mask entries to the
ring. This is used to map incoming sequences to a particular ring whose
RC_CTL/TYPE mask entry matches that of the sequence. The driver should not
attempt to configure a ring whose number is greater than the number
specified in the Port Control Block (PCB). It is an error to issue the
configure ring command more than once with the same ring number. The HBA
returns an error if the driver attempts this.

This routine prepares the mailbox command for configuring IOCB ring.

.. _`lpfc_config_port`:

lpfc_config_port
================

.. c:function:: void lpfc_config_port(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for configuring port

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_config_port.description`:

Description
-----------

The configure port mailbox command is used to identify the Port Control
Block (PCB) in the driver memory. After this command is issued, the
driver must not access the mailbox in the HBA without first resetting
the HBA. The HBA may copy the PCB information to internal storage for
subsequent use; the driver can not change the PCB information unless it
resets the HBA.

This routine prepares the mailbox command for configuring port.

.. _`lpfc_kill_board`:

lpfc_kill_board
===============

.. c:function:: void lpfc_kill_board(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Prepare a mailbox command for killing board

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_kill_board.description`:

Description
-----------

The kill board mailbox command is used to tell firmware to perform a
graceful shutdown of a channel on a specified board to prepare for reset.
When the kill board mailbox command is received, the ER3 bit is set to 1
in the Host Status register and the ER Attention bit is set to 1 in the
Host Attention register of the HBA function that received the kill board
command.

This routine prepares the mailbox command for killing the board in
preparation for a graceful shutdown.

.. _`lpfc_mbox_put`:

lpfc_mbox_put
=============

.. c:function:: void lpfc_mbox_put(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbq)

    Put a mailbox cmd into the tail of driver's mailbox queue

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbq:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_mbox_put.description`:

Description
-----------

Driver maintains a internal mailbox command queue implemented as a linked
list. When a mailbox command is issued, it shall be put into the mailbox
command queue such that they shall be processed orderly as HBA can process
one mailbox command at a time.

.. _`lpfc_mbox_get`:

lpfc_mbox_get
=============

.. c:function:: LPFC_MBOXQ_t *lpfc_mbox_get(struct lpfc_hba *phba)

    Remove a mailbox cmd from the head of driver's mailbox queue

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_mbox_get.description`:

Description
-----------

Driver maintains a internal mailbox command queue implemented as a linked
list. When a mailbox command is issued, it shall be put into the mailbox
command queue such that they shall be processed orderly as HBA can process
one mailbox command at a time. After HBA finished processing a mailbox
command, the driver will remove a pending mailbox command from the head of
the mailbox command queue and send to the HBA for processing.

Return codes
pointer to the driver internal queue element for mailbox command.

.. _`__lpfc_mbox_cmpl_put`:

\__lpfc_mbox_cmpl_put
=====================

.. c:function:: void __lpfc_mbox_cmpl_put(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbq)

    Put mailbox cmd into mailbox cmd complete list

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbq:
        pointer to the driver internal queue element for mailbox command.

.. _`__lpfc_mbox_cmpl_put.description`:

Description
-----------

This routine put the completed mailbox command into the mailbox command
complete list. This is the unlocked version of the routine. The mailbox
complete list is used by the driver worker thread to process mailbox
complete callback functions outside the driver interrupt handler.

.. _`lpfc_mbox_cmpl_put`:

lpfc_mbox_cmpl_put
==================

.. c:function:: void lpfc_mbox_cmpl_put(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbq)

    Put mailbox command into mailbox command complete list

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbq:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_mbox_cmpl_put.description`:

Description
-----------

This routine put the completed mailbox command into the mailbox command
complete list. This is the locked version of the routine. The mailbox
complete list is used by the driver worker thread to process mailbox
complete callback functions outside the driver interrupt handler.

.. _`lpfc_mbox_cmd_check`:

lpfc_mbox_cmd_check
===================

.. c:function:: int lpfc_mbox_cmd_check(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Check the validality of a mailbox command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_mbox_cmd_check.description`:

Description
-----------

This routine is to check whether a mailbox command is valid to be issued.
This check will be performed by both the mailbox issue API when a client
is to issue a mailbox command to the mailbox transport.

Return 0 - pass the check, -ENODEV - fail the check

.. _`lpfc_mbox_dev_check`:

lpfc_mbox_dev_check
===================

.. c:function:: int lpfc_mbox_dev_check(struct lpfc_hba *phba)

    Check the device state for issuing a mailbox command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_mbox_dev_check.description`:

Description
-----------

This routine is to check whether the HBA device is ready for posting a
mailbox command. It is used by the mailbox transport API at the time the
to post a mailbox command to the device.

Return 0 - pass the check, -ENODEV - fail the check

.. _`lpfc_mbox_tmo_val`:

lpfc_mbox_tmo_val
=================

.. c:function:: int lpfc_mbox_tmo_val(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Retrieve mailbox command timeout value

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        *undescribed*

.. _`lpfc_mbox_tmo_val.description`:

Description
-----------

This routine retrieves the proper timeout value according to the mailbox
command code.

Return codes
Timeout value to be used for the given mailbox command

.. _`lpfc_sli4_mbx_sge_set`:

lpfc_sli4_mbx_sge_set
=====================

.. c:function:: void lpfc_sli4_mbx_sge_set(struct lpfcMboxq *mbox, uint32_t sgentry, dma_addr_t phyaddr, uint32_t length)

    Set a sge entry in non-embedded mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command.

    :param uint32_t sgentry:
        sge entry index.

    :param dma_addr_t phyaddr:
        physical address for the sge

    :param uint32_t length:
        Length of the sge.

.. _`lpfc_sli4_mbx_sge_set.description`:

Description
-----------

This routine sets up an entry in the non-embedded mailbox command at the sge
index location.

.. _`lpfc_sli4_mbx_sge_get`:

lpfc_sli4_mbx_sge_get
=====================

.. c:function:: void lpfc_sli4_mbx_sge_get(struct lpfcMboxq *mbox, uint32_t sgentry, struct lpfc_mbx_sge *sge)

    Get a sge entry from non-embedded mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command.

    :param uint32_t sgentry:
        sge entry index.

    :param struct lpfc_mbx_sge \*sge:
        *undescribed*

.. _`lpfc_sli4_mbx_sge_get.description`:

Description
-----------

This routine gets an entry from the non-embedded mailbox command at the sge
index location.

.. _`lpfc_sli4_mbox_cmd_free`:

lpfc_sli4_mbox_cmd_free
=======================

.. c:function:: void lpfc_sli4_mbox_cmd_free(struct lpfc_hba *phba, struct lpfcMboxq *mbox)

    Free a sli4 mailbox command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command.

.. _`lpfc_sli4_mbox_cmd_free.description`:

Description
-----------

This routine frees SLI4 specific mailbox command for sending IOCTL command.

.. _`lpfc_sli4_config`:

lpfc_sli4_config
================

.. c:function:: int lpfc_sli4_config(struct lpfc_hba *phba, struct lpfcMboxq *mbox, uint8_t subsystem, uint8_t opcode, uint32_t length, bool emb)

    Initialize the  SLI4 Config Mailbox command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command.

    :param uint8_t subsystem:
        The sli4 config sub mailbox subsystem.

    :param uint8_t opcode:
        The sli4 config sub mailbox command opcode.

    :param uint32_t length:
        Length of the sli4 config mailbox command (including sub-header).

    :param bool emb:
        *undescribed*

.. _`lpfc_sli4_config.description`:

Description
-----------

This routine sets up the header fields of SLI4 specific mailbox command
for sending IOCTL command.

.. _`lpfc_sli4_config.return`:

Return
------

the actual length of the mbox command allocated (mostly useful
for none embedded mailbox command).

.. _`lpfc_sli4_mbox_rsrc_extent`:

lpfc_sli4_mbox_rsrc_extent
==========================

.. c:function:: int lpfc_sli4_mbox_rsrc_extent(struct lpfc_hba *phba, struct lpfcMboxq *mbox, uint16_t exts_count, uint16_t rsrc_type, bool emb)

    Initialize the opcode resource extent.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfcMboxq \*mbox:
        pointer to an allocated lpfc mbox resource.

    :param uint16_t exts_count:
        the number of extents, if required, to allocate.

    :param uint16_t rsrc_type:
        the resource extent type.

    :param bool emb:
        true if LPFC_SLI4_MBX_EMBED. false if LPFC_SLI4_MBX_NEMBED.

.. _`lpfc_sli4_mbox_rsrc_extent.description`:

Description
-----------

This routine completes the subcommand header for SLI4 resource extent
mailbox commands.  It is called after lpfc_sli4_config.  The caller must
pass an allocated mailbox and the attributes required to initialize the
mailbox correctly.

.. _`lpfc_sli4_mbox_rsrc_extent.return`:

Return
------

the actual length of the mbox command allocated.

.. _`lpfc_sli_config_mbox_subsys_get`:

lpfc_sli_config_mbox_subsys_get
===============================

.. c:function:: uint8_t lpfc_sli_config_mbox_subsys_get(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbox)

    Get subsystem from a sli_config mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbox:
        pointer to lpfc mbox command queue entry.

.. _`lpfc_sli_config_mbox_subsys_get.description`:

Description
-----------

This routine gets the subsystem from a SLI4 specific SLI_CONFIG mailbox
command. If the mailbox command is not MBX_SLI4_CONFIG (0x9B) or if the
sub-header is not present, subsystem LPFC_MBOX_SUBSYSTEM_NA (0x0) shall
be returned.

.. _`lpfc_sli_config_mbox_opcode_get`:

lpfc_sli_config_mbox_opcode_get
===============================

.. c:function:: uint8_t lpfc_sli_config_mbox_opcode_get(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbox)

    Get opcode from a sli_config mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbox:
        pointer to lpfc mbox command queue entry.

.. _`lpfc_sli_config_mbox_opcode_get.description`:

Description
-----------

This routine gets the opcode from a SLI4 specific SLI_CONFIG mailbox
command. If the mailbox command is not MBX_SLI4_CONFIG (0x9B) or if
the sub-header is not present, opcode LPFC_MBOX_OPCODE_NA (0x0) be
returned.

.. _`lpfc_sli4_mbx_read_fcf_rec`:

lpfc_sli4_mbx_read_fcf_rec
==========================

.. c:function:: int lpfc_sli4_mbx_read_fcf_rec(struct lpfc_hba *phba, struct lpfcMboxq *mboxq, uint16_t fcf_index)

    Allocate and construct read fcf mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfcMboxq \*mboxq:
        *undescribed*

    :param uint16_t fcf_index:
        index to fcf table.

.. _`lpfc_sli4_mbx_read_fcf_rec.description`:

Description
-----------

This routine routine allocates and constructs non-embedded mailbox command
for reading a FCF table entry referred by \ ``fcf_index``\ .

.. _`lpfc_sli4_mbx_read_fcf_rec.return`:

Return
------

pointer to the mailbox command constructed if successful, otherwise
NULL.

.. _`lpfc_request_features`:

lpfc_request_features
=====================

.. c:function:: void lpfc_request_features(struct lpfc_hba *phba, struct lpfcMboxq *mboxq)

    Configure SLI4 REQUEST_FEATURES mailbox

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfcMboxq \*mboxq:
        pointer to lpfc mbox command.

.. _`lpfc_request_features.description`:

Description
-----------

This routine sets up the mailbox for an SLI4 REQUEST_FEATURES
mailbox command.

.. _`lpfc_init_vfi`:

lpfc_init_vfi
=============

.. c:function:: void lpfc_init_vfi(struct lpfcMboxq *mbox, struct lpfc_vport *vport)

    Initialize the INIT_VFI mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param struct lpfc_vport \*vport:
        Vport associated with the VF.

.. _`lpfc_init_vfi.description`:

Description
-----------

This routine initializes \ ``mbox``\  to all zeros and then fills in the mailbox
fields from \ ``vport``\ . INIT_VFI configures virtual fabrics identified by VFI
in the context of an FCF. The driver issues this command to setup a VFI
before issuing a FLOGI to login to the VSAN. The driver should also issue a
REG_VFI after a successful VSAN login.

.. _`lpfc_reg_vfi`:

lpfc_reg_vfi
============

.. c:function:: void lpfc_reg_vfi(struct lpfcMboxq *mbox, struct lpfc_vport *vport, dma_addr_t phys)

    Initialize the REG_VFI mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param struct lpfc_vport \*vport:
        vport associated with the VF.

    :param dma_addr_t phys:
        BDE DMA bus address used to send the service parameters to the HBA.

.. _`lpfc_reg_vfi.description`:

Description
-----------

This routine initializes \ ``mbox``\  to all zeros and then fills in the mailbox
fields from \ ``vport``\ , and uses \ ``buf``\  as a DMAable buffer to send the vport's
fc service parameters to the HBA for this VFI. REG_VFI configures virtual
fabrics identified by VFI in the context of an FCF.

.. _`lpfc_init_vpi`:

lpfc_init_vpi
=============

.. c:function:: void lpfc_init_vpi(struct lpfc_hba *phba, struct lpfcMboxq *mbox, uint16_t vpi)

    Initialize the INIT_VPI mailbox command

    :param struct lpfc_hba \*phba:
        pointer to the hba structure to init the VPI for.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param uint16_t vpi:
        VPI to be initialized.

.. _`lpfc_init_vpi.description`:

Description
-----------

The INIT_VPI mailbox command supports virtual N_Ports. The driver uses the
command to activate a virtual N_Port. The HBA assigns a MAC address to use
with the virtual N Port.  The SLI Host issues this command before issuing a
FDISC to connect to the Fabric. The SLI Host should issue a REG_VPI after a
successful virtual NPort login.

.. _`lpfc_unreg_vfi`:

lpfc_unreg_vfi
==============

.. c:function:: void lpfc_unreg_vfi(struct lpfcMboxq *mbox, struct lpfc_vport *vport)

    Initialize the UNREG_VFI mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param struct lpfc_vport \*vport:
        vport associated with the VF.

.. _`lpfc_unreg_vfi.description`:

Description
-----------

The UNREG_VFI mailbox command causes the SLI Host to put a virtual fabric
(logical NPort) into the inactive state. The SLI Host must have logged out
and unregistered all remote N_Ports to abort any activity on the virtual
fabric. The SLI Port posts the mailbox response after marking the virtual
fabric inactive.

.. _`lpfc_sli4_dump_cfg_rg23`:

lpfc_sli4_dump_cfg_rg23
=======================

.. c:function:: int lpfc_sli4_dump_cfg_rg23(struct lpfc_hba *phba, struct lpfcMboxq *mbox)

    Dump sli4 port config region 23

    :param struct lpfc_hba \*phba:
        pointer to the hba structure containing.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

.. _`lpfc_sli4_dump_cfg_rg23.description`:

Description
-----------

This function create a SLI4 dump mailbox command to dump configure
region 23.

.. _`lpfc_reg_fcfi`:

lpfc_reg_fcfi
=============

.. c:function:: void lpfc_reg_fcfi(struct lpfc_hba *phba, struct lpfcMboxq *mbox)

    Initialize the REG_FCFI mailbox command

    :param struct lpfc_hba \*phba:
        pointer to the hba structure containing the FCF index and RQ ID.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

.. _`lpfc_reg_fcfi.description`:

Description
-----------

The REG_FCFI mailbox command supports Fibre Channel Forwarders (FCFs). The
SLI Host uses the command to activate an FCF after it has acquired FCF
information via a READ_FCF mailbox command. This mailbox command also is used
to indicate where received unsolicited frames from this FCF will be sent. By
default this routine will set up the FCF to forward all unsolicited frames
the the RQ ID passed in the \ ``phba``\ . This can be overridden by the caller for
more complicated setups.

.. _`lpfc_reg_fcfi_mrq`:

lpfc_reg_fcfi_mrq
=================

.. c:function:: void lpfc_reg_fcfi_mrq(struct lpfc_hba *phba, struct lpfcMboxq *mbox, int mode)

    Initialize the REG_FCFI_MRQ mailbox command

    :param struct lpfc_hba \*phba:
        pointer to the hba structure containing the FCF index and RQ ID.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param int mode:
        0 to register FCFI, 1 to register MRQs

.. _`lpfc_reg_fcfi_mrq.description`:

Description
-----------

The REG_FCFI_MRQ mailbox command supports Fibre Channel Forwarders (FCFs).
The SLI Host uses the command to activate an FCF after it has acquired FCF
information via a READ_FCF mailbox command. This mailbox command also is used
to indicate where received unsolicited frames from this FCF will be sent. By
default this routine will set up the FCF to forward all unsolicited frames
the the RQ ID passed in the \ ``phba``\ . This can be overridden by the caller for
more complicated setups.

.. _`lpfc_unreg_fcfi`:

lpfc_unreg_fcfi
===============

.. c:function:: void lpfc_unreg_fcfi(struct lpfcMboxq *mbox, uint16_t fcfi)

    Initialize the UNREG_FCFI mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param uint16_t fcfi:
        FCFI to be unregistered.

.. _`lpfc_unreg_fcfi.description`:

Description
-----------

The UNREG_FCFI mailbox command supports Fibre Channel Forwarders (FCFs).
The SLI Host uses the command to inactivate an FCFI.

.. _`lpfc_resume_rpi`:

lpfc_resume_rpi
===============

.. c:function:: void lpfc_resume_rpi(struct lpfcMboxq *mbox, struct lpfc_nodelist *ndlp)

    Initialize the RESUME_RPI mailbox command

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

    :param struct lpfc_nodelist \*ndlp:
        The nodelist structure that describes the RPI to resume.

.. _`lpfc_resume_rpi.description`:

Description
-----------

The RESUME_RPI mailbox command is used to restart I/O to an RPI after a
link event.

.. _`lpfc_supported_pages`:

lpfc_supported_pages
====================

.. c:function:: void lpfc_supported_pages(struct lpfcMboxq *mbox)

    Initialize the PORT_CAPABILITIES supported pages mailbox command.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

.. _`lpfc_supported_pages.description`:

Description
-----------

The PORT_CAPABILITIES supported pages mailbox command is issued to
retrieve the particular feature pages supported by the port.

.. _`lpfc_pc_sli4_params`:

lpfc_pc_sli4_params
===================

.. c:function:: void lpfc_pc_sli4_params(struct lpfcMboxq *mbox)

    Initialize the PORT_CAPABILITIES SLI4 Params mbox cmd.

    :param struct lpfcMboxq \*mbox:
        pointer to lpfc mbox command to initialize.

.. _`lpfc_pc_sli4_params.description`:

Description
-----------

The PORT_CAPABILITIES SLI4 parameters mailbox command is issued to
retrieve the particular SLI4 features supported by the port.

.. This file was automatic generated / don't edit.

