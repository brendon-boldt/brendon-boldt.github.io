let current = document.currentScript.getAttribute('data-current');
let currentObj = {};
currentObj[current] = 'current';
let headerHtml = `
<div id="header">

	<!-- Logo -->
	<h1><a href="index.html" id="logo">Brendon Boldt<em>: Computer Scientist, Philosopher, Machine Teacher</em></a></h1>

	<!-- Nav -->
		<nav id="nav">
			<ul>
				<li class="${currentObj['home']}"><a href="index.html">Home</a></li>
				<li class="${currentObj['research']}"><a href="research.html">Computer Science</a></li>
				<li class="${currentObj['philosophy']}"><a href="#">Philosophy</a></li>
				<li class="${currentObj['contact']}"><a href="#footer">Contact</a></li>
				<!--
				<li>
					<a href="#">Dropdown</a>
					<ul>
						<li><a href="#">Lorem dolor</a></li>
						<li><a href="#">Magna phasellus</a></li>
						<li><a href="#">Etiam sed tempus</a></li>
						<li>
							<a href="#">Submenu</a>
							<ul>
								<li><a href="#">Lorem dolor</a></li>
								<li><a href="#">Phasellus magna</a></li>
								<li><a href="#">Magna phasellus</a></li>
								<li><a href="#">Etiam nisl</a></li>
								<li><a href="#">Veroeros feugiat</a></li>
							</ul>
						</li>
						<li><a href="#">Veroeros feugiat</a></li>
					</ul>
				</li>
				<li><a href="left-sidebar.html">Left Sidebar</a></li>
				<li><a href="right-sidebar.html">Right Sidebar</a></li>
				<li><a href="two-sidebar.html">Two Sidebar</a></li>
				<li><a href="no-sidebar.html">No Sidebar</a></li>
				-->
			</ul>
		</nav>

</div>
`;
document.write(headerHtml);
