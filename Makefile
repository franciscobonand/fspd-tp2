config:
	chmod +x svc_arm.py
	chmod +x cln_arm.py
	chmod +x svc_comp.py
	chmod +x cln_comp.py

run_serv_arm:
	./svc_arm.py $(arg)
run_cli_arm:
	./cln_arm.py $(arg)
run_serv_comp:
	./svc_comp.py $(arg1) $(arg2) $(arg3)
run_cli_comp:
	./cln_comp.py $(arg)

clean:
	rm -rf __pycache__