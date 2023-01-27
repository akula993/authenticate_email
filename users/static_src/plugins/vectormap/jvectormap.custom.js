$(function () {
	"use strict";
	jQuery('#world-map-markers').vectorMap({
		map: 'world_mill_en',
		backgroundColor: 'transparent',
		borderColor: '#818181',
		borderOpacity: 0.25,
		borderWidth: 1,
		zoomOnScroll: false,
		color: '#009efb',
		regionStyle: {
			initial: {
				fill: '#923eb9'
			}
		},
		markerStyle: {
			initial: {
				r: 9,
				'fill': '#fff',
				'fill-opacity': 1,
				'stroke': '#000',
				'stroke-width': 5,
				'stroke-opacity': 0.4
			},
		},
		enableZoom: true,
		hoverColor: '#009efb',
		markers: [{
			latLng: [50.00, 40.00],
			name: 'I Love My India'
		}],
		hoverOpacity: null,
		normalizeFunction: 'linear',
		scaleColors: ['#b6d6ff', '#005ace'],
		selectedColor: '#c9dfaf',
		selectedRegions: [],
		showTooltip: true,
		onRegionClick: function (element, code, region) {
			var message = 'Вы нажали "' + region + '" который имеет код: ' + code.toUpperCase();
			alert(message);
		}
	});
	$('#india').vectorMap({
		map: 'in_mill',
		backgroundColor: 'transparent',
		zoomOnScroll: false,
		regionStyle: {
			initial: {
				fill: '#32bfff'
			}
		}
	});
	$('#usa').vectorMap({
		map: 'us_aea_en',
		backgroundColor: 'transparent',
		zoomOnScroll: false,
		regionStyle: {
			initial: {
				fill: '#f73757'
			}
		}
	});
	$('#australia').vectorMap({
		map: 'au_mill',
		backgroundColor: 'transparent',
		zoomOnScroll: false,
		regionStyle: {
			initial: {
				fill: '#ffab4d'
			}
		}
	});
	$('#uk').vectorMap({
		map: 'uk_mill_en',
		backgroundColor: 'transparent',
		zoomOnScroll: false,
		regionStyle: {
			initial: {
				fill: '#18bb6b'
			}
		}
	});
});