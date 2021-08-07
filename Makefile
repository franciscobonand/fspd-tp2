run_serv_arm:
	chmod +x svc_arm.py
	./svc_arm.py $(arg)
run_cli_arm:
	chmod +x cln_arm.py
	./cln_arm.py $(arg)
run_serv_comp:
	chmod +x svc_comp.py
	./svc_comp.py $(arg1) $(arg2) $(arg3)
run_cli_comp:
	chmod +x cln_comp.py
	./cln_comp.py $(arg)

clean:
	rm -rf __pycache__