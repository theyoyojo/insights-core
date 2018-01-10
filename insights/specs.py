from insights.core.spec_factory import SpecSet, RegistryPoint


class Specs(SpecSet):
    autofs_conf = RegistryPoint(alias="autofs.conf")
    audit_log = RegistryPoint()
    auditd_conf = RegistryPoint(alias="auditd.conf")
    blkid = RegistryPoint()
    bond = RegistryPoint()
    branch_info = RegistryPoint()
    brctl_show = RegistryPoint()
    candlepin_log = RegistryPoint(alias="candlepin.log")
    candlepin_error_log = RegistryPoint()
    ps_auxww = RegistryPoint()
    catalina_out = RegistryPoint(alias="catalina.out")
    catalina_server_log = RegistryPoint()
    cciss = RegistryPoint()
    ceilometer_central_log = RegistryPoint()
    ceilometer_collector_log = RegistryPoint()
    ceilometer_conf = RegistryPoint(alias="ceilometer.conf")
    ceph_socket_files = RegistryPoint()
    ceph_config_show = RegistryPoint()
    ceph_df_detail = RegistryPoint()
    ceph_health_detail = RegistryPoint()
    ceph_osd_dump = RegistryPoint()
    ceph_osd_df = RegistryPoint()
    ceph_osd_ec_profile_ls = RegistryPoint()
    ceph_osd_ec_profile_get = RegistryPoint()
    ceph_osd_log = RegistryPoint(alias="ceph_osd.log")
    ceph_osd_tree = RegistryPoint()
    ceph_s = RegistryPoint()
    ceph_v = RegistryPoint()
    certificates_enddate = RegistryPoint()
    chkconfig = RegistryPoint()
    chrony_conf = RegistryPoint(alias="chrony.conf")
    chronyc_sources = RegistryPoint()
    cib_xml = RegistryPoint(alias="cib.xml")
    cinder_conf = RegistryPoint(alias="cinder.conf")
    cinder_volume_log = RegistryPoint(alias="cinder_volume.log")
    cluster_conf = RegistryPoint(alias="cluster.conf")
    cmdline = RegistryPoint()
    cpe = RegistryPoint()
    cobbler_settings = RegistryPoint()
    cobbler_modules_conf = RegistryPoint(alias="cobbler_modules.conf")
    corosync = RegistryPoint()
    cpuinfo = RegistryPoint()
    cpuinfo_max_freq = RegistryPoint()
    current_clocksource = RegistryPoint()
    date = RegistryPoint()
    date_iso = RegistryPoint()
    date_utc = RegistryPoint()
    df__al = RegistryPoint(alias="df_-al")
    df__alP = RegistryPoint(alias="df_-alP")
    df__li = RegistryPoint(alias="df_-li")
    dig = RegistryPoint()
    dig_dnssec = RegistryPoint()
    dig_edns = RegistryPoint()
    dig_noedns = RegistryPoint()
    dirsrv = RegistryPoint()
    dirsrv_access = RegistryPoint()
    dirsrv_errors = RegistryPoint()
    display_java = RegistryPoint()
    dmesg = RegistryPoint()
    dmidecode = RegistryPoint()
    docker_info = RegistryPoint()
    docker_list_containers = RegistryPoint()
    docker_list_images = RegistryPoint()
    docker_host_machine_id = RegistryPoint()
    docker_image_inspect = RegistryPoint()
    docker_container_inspect = RegistryPoint()
    docker_network = RegistryPoint()
    docker_storage = RegistryPoint()
    docker_storage_setup = RegistryPoint()
    docker_sysconfig = RegistryPoint()
    dumpdev = RegistryPoint()
    dumpe2fs_h = RegistryPoint(alias="dumpe2fs-h")
    engine_log = RegistryPoint(alias="engine.log")
    etc_journald_conf = RegistryPoint(alias="etc_journald.conf")
    etc_journald_conf_d = RegistryPoint(alias="etc_journald.conf.d")
    ethernet_interfaces = RegistryPoint()
    dcbtool_gc_dcb = RegistryPoint()
    ethtool = RegistryPoint()
    ethtool_S = RegistryPoint(alias="ethtool-S")
    ethtool_a = RegistryPoint(alias="ethtool-a")
    ethtool_c = RegistryPoint(alias="ethtool-c")
    ethtool_g = RegistryPoint(alias="ethtool-g")
    ethtool_i = RegistryPoint(alias="ethtool-i")
    ethtool_k = RegistryPoint(alias="ethtool-k")
    exim_conf = RegistryPoint(alias="exim.conf")
    facter = RegistryPoint()
    fc_match = RegistryPoint(alias="fc-match")
    fdisk_l = RegistryPoint(alias="fdisk-l")
    fdisk_l_sos = RegistryPoint()
    foreman_production_log = RegistryPoint(alias="foreman_production.log")
    foreman_proxy_conf = RegistryPoint()
    foreman_proxy_log = RegistryPoint(alias="foreman_proxy.log")
    foreman_satellite_log = RegistryPoint(alias="foreman_satellite.log")
    foreman_ssl_access_ssl_log = RegistryPoint(alias="foreman-ssl_access_ssl.log")
    fstab = RegistryPoint()
    galera_cnf = RegistryPoint(alias="galera.cnf")
    getcert_list = RegistryPoint()
    getenforce = RegistryPoint()
    getsebool = RegistryPoint()
    glance_api_conf = RegistryPoint("glance-api.conf")
    glance_api_log = RegistryPoint()
    glance_cache_conf = RegistryPoint("glance-cache.conf")
    glance_registry_conf = RegistryPoint("glance-registry.conf")
    grub_conf = RegistryPoint("grub.conf")
    grub_efi_conf = RegistryPoint("grub-efi.conf")
    grub2_cfg = RegistryPoint("grub2.cfg")
    grub2_efi_cfg = RegistryPoint("grub2-efi.cfg")
    grub_config_perms = RegistryPoint()
    grub1_config_perms = RegistryPoint()
    hammer_ping = RegistryPoint()
    haproxy_cfg = RegistryPoint()
    heat_api_log = RegistryPoint("heat-api.log")
    heat_conf = RegistryPoint("heat.conf")
    heat_crontab = RegistryPoint()
    heat_engine_log = RegistryPoint("heat-engine.log")
    hostname = RegistryPoint()
    hosts = RegistryPoint()
    hponcfg_g = RegistryPoint("hponcfg-g")
    httpd_access_log = RegistryPoint()
    httpd_conf = RegistryPoint()
    httpd_conf_sos = RegistryPoint()
    httpd_error_log = RegistryPoint()
    httpd_pid = RegistryPoint()
    httpd_limits = RegistryPoint()
    httpd_ssl_access_log = RegistryPoint()
    httpd_ssl_error_log = RegistryPoint()
    httpd_V = RegistryPoint("httpd-V")
    ifcfg = RegistryPoint()
    ifconfig = RegistryPoint()
    imagemagick_policy = RegistryPoint()
    init_ora = RegistryPoint("init.ora")
    initscript = RegistryPoint()
    interrupts = RegistryPoint()
    ip_addr = RegistryPoint()
    ip_route_show_table_all = RegistryPoint()
    ip_s_link = RegistryPoint("ip-s_link")
    ipaupgrade_log = RegistryPoint()
    ipcs_s = RegistryPoint()
    semid = RegistryPoint()
    ipcs_s_i = RegistryPoint()
    iptables = RegistryPoint()
    iptables_permanent = RegistryPoint()
    ip6tables = RegistryPoint()
    ip6tables_permanent = RegistryPoint()
    ipv4_neigh = RegistryPoint()
    ipv6_neigh = RegistryPoint()
    iscsiadm_m_session = RegistryPoint()
    journal_since_boot = RegistryPoint()
    katello_service_status = RegistryPoint("katello-service_status")
    kdump = RegistryPoint()
    kdump_conf = RegistryPoint("kdump.conf")
    kerberos_kdc_log = RegistryPoint()
    kexec_crash_loaded = RegistryPoint()
    kexec_crash_size = RegistryPoint()
    keystone_conf = RegistryPoint("keystone.conf")
    keystone_crontab = RegistryPoint()
    keystone_log = RegistryPoint("keystone.log")
    krb5 = RegistryPoint()
    ksmstate = RegistryPoint()
    last_upload_globs = RegistryPoint()
    lastupload = RegistryPoint()
    libkeyutils = RegistryPoint()
    libkeyutils_objdumps = RegistryPoint()
    libvirtd_log = RegistryPoint("libvirtd.log")
    limits_conf = RegistryPoint()
    locale = RegistryPoint()
    localtime = RegistryPoint()
    lpstat_p = RegistryPoint()
    lsblk = RegistryPoint()
    lsblk_pairs = RegistryPoint()
    lscpu = RegistryPoint()
    lsinitrd_lvm_conf = RegistryPoint("lsinitrd_lvm.conf")
    lsmod = RegistryPoint()
    lspci = RegistryPoint()
    lsof = RegistryPoint()
    lssap = RegistryPoint()
    ls_boot = RegistryPoint()
    ls_docker_volumes = RegistryPoint()
    ls_dev = RegistryPoint()
    ls_disk = RegistryPoint()
    ls_etc = RegistryPoint()
    ls_sys_firmware = RegistryPoint()
    ls_var_log = RegistryPoint()
    ls_var_www = RegistryPoint()
    lvdisplay = RegistryPoint()
    lvm_conf = RegistryPoint("lvm.conf")
    lvs = RegistryPoint()
    lvs_noheadings = RegistryPoint()
    machine_id = RegistryPoint("machine-id")
    manila_conf = RegistryPoint()
    mariadb_log = RegistryPoint("mariadb.log")
    mdstat = RegistryPoint()
    meminfo = RegistryPoint()
    messages = RegistryPoint()
    metadata_json = RegistryPoint()
    mlx4_port = RegistryPoint()
    module = RegistryPoint()
    modinfo = RegistryPoint()
    modprobe_conf = RegistryPoint("modprobe.conf")
    sysconfig_mongod = RegistryPoint()
    mongod_conf = RegistryPoint()
    modprobe_d = RegistryPoint("modprobe.d")
    mount = RegistryPoint()
    multicast_querier = RegistryPoint()
    multipath_conf = RegistryPoint("multipath.conf")
    multipath__v4__ll = RegistryPoint("multipath_-v4_-ll")
    named_checkconf_p = RegistryPoint("named-checkconf_p")
    netconsole = RegistryPoint()
    netstat = RegistryPoint()
    netstat_agn = RegistryPoint("netstat_-agn")
    netstat_i = RegistryPoint("netstat-i")
    netstat_s = RegistryPoint("netstat-s")
    neutron_conf = RegistryPoint("neutron.conf")
    neutron_ovs_agent_log = RegistryPoint()
    neutron_plugin_ini = RegistryPoint("neutron_plugin.ini")
    neutron_server_log = RegistryPoint()
    nfnetlink_queue = RegistryPoint()
    nfs_exports = RegistryPoint()
    nfs_exports_d = RegistryPoint("nfs_exports.d")
    nginx_conf = RegistryPoint()
    nova_api_log = RegistryPoint("nova-api_log")
    nova_compute_log = RegistryPoint("nova-compute.log")
    nova_conf = RegistryPoint("nova.conf")
    nova_crontab = RegistryPoint()
    nscd_conf = RegistryPoint("nscd.conf")
    nsswitch_conf = RegistryPoint("nsswitch.conf")
    ntp_conf = RegistryPoint("ntp.conf")
    ntpq_leap = RegistryPoint()
    ntpq_pn = RegistryPoint()
    ntptime = RegistryPoint()
    numeric_user_group_name = RegistryPoint()
    oc_get_pod = RegistryPoint()
    oc_get_bc = RegistryPoint()
    oc_get_dc = RegistryPoint()
    oc_get_endpoints = RegistryPoint()
    oc_get_service = RegistryPoint()
    oc_get_rolebinding = RegistryPoint()
    oc_get_project = RegistryPoint()
    oc_get_role = RegistryPoint()
    oc_get_pv = RegistryPoint()
    oc_get_pvc = RegistryPoint()
    crt = RegistryPoint()
    openshift_certificates = RegistryPoint()
    openvswitch_server_log = RegistryPoint()
    openvswitch_daemon_log = RegistryPoint()
    os_release = RegistryPoint("os-release")
    osa_dispatcher_log = RegistryPoint("osa_dispatcher.log")
    ose_master_config = RegistryPoint()
    ose_node_config = RegistryPoint()
    ovirt_engine_confd = RegistryPoint()
    ovirt_engine_server_log = RegistryPoint("ovirt_engine_server.log")
    ovs_vsctl_show = RegistryPoint("ovs-vsctl_show")
    pacemaker_log = RegistryPoint("pacemaker.log")
    running_java = RegistryPoint()
    package_provides_java = RegistryPoint()
    pam_conf = RegistryPoint("pam.conf")
    parted__l = RegistryPoint("parted_-l")
    password_auth = RegistryPoint("password-auth")
    pcs_status = RegistryPoint()
    pluginconf_d = RegistryPoint("pluginconf.d")
    postgresql_conf = RegistryPoint("postgresql.conf")
    postgresql_log = RegistryPoint()
    md5chk_files = RegistryPoint()
    prelink_orig_md5 = RegistryPoint()
    prev_uploader_log = RegistryPoint()
    proc_snmp_ipv4 = RegistryPoint()
    puppet_ssl_cert_ca_pem = RegistryPoint()
    pvs = RegistryPoint()
    pvs_noheadings = RegistryPoint()
    qemu_conf = RegistryPoint("qemu.conf")
    qpid_stat_q = RegistryPoint()
    qpid_stat_u = RegistryPoint()
    rabbitmq_logs = RegistryPoint()
    rabbitmq_policies = RegistryPoint()
    rabbitmq_queues = RegistryPoint()
    rabbitmq_report = RegistryPoint()
    rabbitmq_startup_err = RegistryPoint()
    rabbitmq_startup_log = RegistryPoint()
    rabbitmq_users = RegistryPoint()
    rc_local = RegistryPoint("rc.local")
    redhat_release = RegistryPoint("redhat-release")
    resolv_conf = RegistryPoint("resolv.conf")
    rhn_charsets = RegistryPoint("rhn-charsets")
    rhn_conf = RegistryPoint("rhn.conf")
    rhn_entitlement_cert_xml = RegistryPoint("rhn-entitlement-cert.xml")
    rhn_hibernate_conf = RegistryPoint("rhn_hibernate.conf")
    rhn_schema_stats = RegistryPoint("rhn-schema-stats")
    rhn_schema_version = RegistryPoint("rhn-schema-version")
    rhn_server_satellite_log = RegistryPoint("rhn_server_satellite.log")
    rhn_server_xmlrpc_log = RegistryPoint("rhn_server_xmlrpc.log")
    rhn_search_daemon_log = RegistryPoint("rhn_search_daemon.log")
    rhn_taskomatic_daemon_log = RegistryPoint("rhn_taskomatic_daemon.log")
    rhsm_conf = RegistryPoint("rhsm.conf")
    rhsm_log = RegistryPoint("rhsm.log")
    root_crontab = RegistryPoint()
    route = RegistryPoint()
    rpm_V_packages = RegistryPoint("rpm_-V_packages")
    rsyslog_conf = RegistryPoint("rsyslog.conf")
    samba = RegistryPoint()
    satellite_version_rb = RegistryPoint("satellite_version.rb")
    block_devices = RegistryPoint()
    scheduler = RegistryPoint()
    scsi = RegistryPoint()
    secure = RegistryPoint()
    selinux_config = RegistryPoint("selinux-config")
    sestatus = RegistryPoint()
    smbstatus_p = RegistryPoint()
    smbstatus_S = RegistryPoint()
    smartctl = RegistryPoint()
    softnet_stat = RegistryPoint()
    spfile_ora = RegistryPoint("spfile.ora")
    ss = RegistryPoint()
    ssh_config = RegistryPoint()
    sshd_config = RegistryPoint()
    sshd_config_perms = RegistryPoint()
    sssd_config = RegistryPoint()
    sssd_logs = RegistryPoint()
    swift_object_expirer_conf = RegistryPoint()
    swift_proxy_server_conf = RegistryPoint()
    sysconfig_chronyd = RegistryPoint()
    sysconfig_httpd = RegistryPoint()
    sysconfig_irqbalance = RegistryPoint()
    sysconfig_kdump = RegistryPoint()
    sysconfig_ntpd = RegistryPoint()
    sysconfig_virt_who = RegistryPoint()
    sysctl = RegistryPoint()
    sysctl_conf = RegistryPoint("sysctl.conf")
    sysctl_conf_initramfs = RegistryPoint("sysctl.conf_initramfs")
    systemctl_cinder_volume = RegistryPoint("systemctl_cinder-volume")
    systemctl_list_unit_files = RegistryPoint("systemctl_list-unit-files")
    systemctl_list_units = RegistryPoint("systemctl_list-units")
    systemctl_mariadb = RegistryPoint()
    systemd_docker = RegistryPoint()
    systemd_openshift_node = RegistryPoint()
    systemd_system_conf = RegistryPoint("systemd_system.conf")
    systemid = RegistryPoint()
    teamdctl_state_dump = RegistryPoint()
    thp_use_zero_page = RegistryPoint()
    thp_enabled = RegistryPoint()
    tmpfilesd = RegistryPoint()
    tomcat_web_xml = RegistryPoint("tomcat_web.xml")
    tomcat_vdc_targeted = RegistryPoint()
    tomcat_vdc_fallback = RegistryPoint()
    tuned_adm = RegistryPoint("tuned-adm")
    udev_persistent_net_rules = RegistryPoint("udev-persistent-net.rules")
    uname = RegistryPoint()
    up2date = RegistryPoint()
    uploader_log = RegistryPoint()
    uptime = RegistryPoint()
    usr_journald_conf_d = RegistryPoint("usr_journald.conf.d")
    vgdisplay = RegistryPoint()
    vdsm_conf = RegistryPoint("vdsm.conf")
    vdsm_id = RegistryPoint()
    vdsm_log = RegistryPoint("vdsm.log")
    vgs = RegistryPoint()
    vgs_noheadings = RegistryPoint()
    virt_what = RegistryPoint("virt-what")
    virt_who_conf = RegistryPoint()
    vmcore_dmesg = RegistryPoint()
    vsftpd = RegistryPoint()
    vsftpd_conf = RegistryPoint("vsftpd.conf")
    woopsie = RegistryPoint()
    xfs_info = RegistryPoint()
    xinetd_conf = RegistryPoint("xinetd.conf")
    yum_conf = RegistryPoint("yum.conf")
    yum_log = RegistryPoint("yum.log")
    yum_repolist = RegistryPoint("yum-repolist")
    yum_repos_d = RegistryPoint("yum.repos.d")
    rpm_format = RegistryPoint()
    host_installed_rpms = RegistryPoint()
    installed_rpms = RegistryPoint("installed-rpms")
    jboss_domain_server_log = RegistryPoint()