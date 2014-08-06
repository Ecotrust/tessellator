VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    config.vm.hostname = "tessellator-dev"

    # config.vm.network "forwarded_port", guest: 80, host: 8080
    config.vm.network :forwarded_port, guest: 8001, host: 8001

    config.vm.provider :virtualbox do |vbox|
        vbox.memory = 1024
        vbox.cpus = 4
        vbox.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
    end

    config.vm.provision "ansible" do |ansible|
        # need a way to specify ansible path to the devops folder 
        ansible.sudo = true
        ansible.playbook = "../devops/provisioning/vagrant.yml"
        ansible.verbose = 'vv'
        ansible.extra_vars = {
            name: 'tessellator',
            app_user: 'tessellator',
            redis: true,
            repo: 'https://github.com/point97/tessellator.git',
            branch: 'master',
            aws_access_key: 'nothing',
            aws_secret: 'nothing',
        }
    end
end