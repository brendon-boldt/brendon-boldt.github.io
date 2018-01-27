let footerHtml = `
<div id="footer">
	<div class="container">
		<div class="row">
			<!--
			<section class="3u 6u(narrower) 12u$(mobilep)">
			-->
			<section class="6u 6u(narrower) 12u$(mobilep)">
				<h3>Links</h3>
				<ul class="links">
					<li><a href="https://github.com/brendon-boldt/brendon-boldt.github.io/tree/master/files/brendon_boldt_cv.pdf">Resume</a></li>
					<li><a href="https://github.com/brendon-boldt/">GitHub</a></li>
					<li><a href="https://www.linkedin.com/in/brendonjboldt/">LinkedIn</a></li>
					<li><a href="https://scholar.google.com/citations?user=QEXlK3AAAAAJ&hl=en&oi=ao">Google Scholar</a></li>
					<li><a href="https://www.researchgate.net/profile/Brendon_Boldt">Research Gate</a></li>
				</ul>
			</section>
			<section class="6u 6u$(narrower) 12u$(mobilep)">
				<h3>Email Haiku</h3>
				Given name, surname<br/>
				and a dot in between at<br/>
				the com of gmail

			</section>
			<!--
			<section class="3u 6u$(narrower) 12u$(mobilep)">
				<h3>More Links to Stuff</h3>
				<ul class="links">
					<li><a href="#">Duis neque nisi dapibus</a></li>
					<li><a href="#">Sed et dapibus quis</a></li>
					<li><a href="#">Rutrum accumsan sed</a></li>
					<li><a href="#">Mattis et sed accumsan</a></li>
					<li><a href="#">Duis neque nisi sed</a></li>
					<li><a href="#">Sed et dapibus quis</a></li>
					<li><a href="#">Rutrum amet varius</a></li>
				</ul>
			</section>
			<section class="6u 12u(narrower)">
				<h3>Get In Touch</h3>
				<form>
					<div class="row 50%">
						<div class="6u 12u(mobilep)">
							<input type="text" name="name" id="name" placeholder="Name" />
						</div>
						<div class="6u 12u(mobilep)">
							<input type="email" name="email" id="email" placeholder="Email" />
						</div>
					</div>
					<div class="row 50%">
						<div class="12u">
							<textarea name="message" id="message" placeholder="Message" rows="5"></textarea>
						</div>
					</div>
					<div class="row 50%">
						<div class="12u">
							<ul class="actions">
								<li><input type="submit" class="button alt" value="Send Message" /></li>
							</ul>
						</div>
					</div>
				</form>
			</section>
			-->
		</div>
	</div>

	<!-- Icons -->
		<ul class="icons">
			<!--
			<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
			<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
			<li><a href="#" class="icon fa-google-plus"><span class="label">Google+</span></a></li>
			-->
			<li><a href="https://github.com/brendon-boldt/" class="icon fa-github"><span class="label">GitHub</span></a></li>
			<li><a href="https://www.linkedin.com/in/brendonjboldt/" class="icon fa-linkedin"><span class="label">LinkedIn</span></a></li>
		</ul>

	<!-- Copyright -->
		<div class="copyright">
			<ul class="menu">
				<li>&copy; Untitled. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
			</ul>
		</div>

</div>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-113184953-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-113184953-1');
</script>
`;
document.write(footerHtml);
